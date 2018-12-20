import numpy as np 
import sys

if len(sys.argv) < 2:
    print("Please pass samples as a parameter!")
    quit()
samples = sys.argv[1]

states = ["rain", "not_rain"]
observations = ["umbrella", "not_umbrella"]


#probability of states given state
transition_model = {
   'rain' : [0.7, 0.3],
   'not_rain' : [0.3, 0.7],
   }

fwd_transition_model = np.array(
    [np.array([0.7, 0.3]),
    np.array([0.3, 0.7])]
)

#probability of observations given state
emission_probability = {
   'rain' : [0.9, 0.1],
   'not_rain' : [0.2, 0.8],
   }

emission_true = np.zeros(shape=(2,2))
emission_true[0][0] = 0.9
emission_true[1][1] = 0.2

emission_false = np.zeros(shape=(2,2))
emission_false[0][0] = 0.1
emission_false[1][1] = 0.8
#c = fattore di normalizzazione (1/somma dei due)

emission = {
    "umbrella" : emission_true,
    "not_umbrella" : emission_false
}

seq_length = 20
sequences = 15

observed = []
actual_states = []

with open(samples, "r") as samples:
    lines = samples.readlines()
    for line in lines:
        observed.append(line.split(":")[1].split(",")[1].strip())
        actual_states.append(line.split(":")[1].split(",")[0].strip())

fwd = []

prev = np.array([0.5, 0.5]).reshape(2,1)
for i in range(seq_length):
    fwd.append(prev)
    marg = (0, 0)
    unnorm = emission[observed[i]].dot(np.transpose(fwd_transition_model)).dot(prev)
    prev = (1.0/(unnorm[0][0] + unnorm[1][0])) * unnorm
    #outfile.write(str(i+1) + ":" + str(prev[0][0]) + "," + str(prev[1][0]) + "\n")

bwd = []

prev = np.array([1.0, 1.0]).reshape(2,1)
for i in range(seq_length):
    bwd.append(prev)
    marg = (0, 0)
    unnorm = np.transpose(fwd_transition_model).dot(emission[observed[i]]).dot(prev)
    prev = (1.0/(unnorm[0][0] + unnorm[1][0])) * unnorm
    #outfile.write(str(i+1) + ":" + str(prev[0][0]) + "," + str(prev[1][0]) + "\n")

marginals = []

with open("marginals.txt", "w") as outfile:
    for i in range(seq_length):
        j = seq_length-1-i

        f = fwd[i]
        b = bwd[j]

        unnorm = np.array([ f[0][0]*b[0][0], f[1][0]*b[1][0] ]).reshape(2,1)
        smooth = (1.0/(unnorm[0][0] + unnorm[1][0])) * unnorm
        outfile.write(str(i+1) + ":" + str(smooth[0][0]) + "," + str(smooth[1][0]) + "\n")
        marginals.append(smooth)

with open("accuracy.txt", "w") as outfile:
    for i in range(seq_length):
        print(marginals[i][0][0])
        print(marginals[i][1][0])
        print(actual_states[i])
        if (marginals[i][0][0] < marginals[i][1][0] and observed[i] == "rain") or (marginals[i][0][0] > marginals[i][1][0] and actual_states[i] == "not_rain"):
            outfile.write(str(i+1) + ":" + "wrong\n")
        else:
            outfile.write(str(i+1) + ":" + "right\n")

