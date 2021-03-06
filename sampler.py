#Copyright (C) 2018 jotaro-sama
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np 

states = ["rain", "not_rain"]
observations = ["umbrella", "not_umbrella"]

#probability of states given state
transition_model = {
   'rain' : [0.7, 0.3],
   'not_rain' : [0.3, 0.7],
   }

#probability of observations given state
emission_probability = {
   'rain' : [0.9, 0.1],
   'not_rain' : [0.2, 0.8],
   }

seq_length = 20
sequences = 15

for j in range(sequences):
    previous  = np.random.choice(a=states)
    with open("samples" + str(j+1) + ".txt", "w") as outfile:
        for i in range(seq_length): 
            umbrella = np.random.choice(a=observations, p=emission_probability[previous])
            outfile.write(str(i+1) + ":" + previous + "," + umbrella + "\n")
            previous = np.random.choice(a=states, p=transition_model[previous])

