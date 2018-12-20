# UmbrellaHMM
An implementation of the umbrella world Hidden Markov Model found in the Russel &amp; Norvig book, with direct samplign and the forward-backward algorithm.

## Requirements
NumPy needs to be installed. On any system with `pip` installed:
```
pip install numpy
```

## Usage
The `sampler.py` script generates a number of sample files, each of which contain a sequence of a certain length (meaning: the events are sampled for some consequent days). You can pass one of those files to `model.py`, which takes it as an input and uses the forward-backward algorithm to calculate the posterior marginals based on the observations only. Marginals are stored in `marginals.txt`. An `accuracy.txt` file is then generated comparing the guesses of the algorithm to the actual event. A "wrong" value doesn't actually mean the marginals are wrong, since it only takes into account whether the algorithm considered one outcome more likely. It only means that the outcome which the algorithm considered less likely happened. If on many tests with different samples there are many more "right" values than "wrong" values, the algorithm is behaving correctly.
