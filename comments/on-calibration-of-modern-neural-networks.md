***

## General comments on paper (8/10):

* really interesting issue discussed, I've never thought about NNs calibration
* a lot of experiments which cover topic

## Comments

* eventually, calibration issue for neural network is really interesting, since it's connected with different aspects of modern NNs performance: first of all, when we work in classification setting, then we expect, that probabilities which we get after softmax have some meaning -- papers showed that it's not the case for NNs and their predictions highly misscalibrated

* another cool thing about this paper is that Temperature Scaling is very good baseline for calibration task: 1) it doesn't change actual model prediction 2) it's extremely easy to implement

* + task of predictions calibration is covered fully in this paper, therefore I find it to be good reference to read (just in case)
