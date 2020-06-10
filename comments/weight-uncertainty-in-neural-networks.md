
[10-06-2020][paper5]
* Weight Uncertainty in Neural Networks
* Charles Blundell, Julien Cornebise, Koray Kavukcuoglu, Daan Wierstra
* `ICML 2015`
* [[Bayesian Methods]](#bayesian-methods) [[Uncertatinty Estimation]](#uncertainty-estimation)

****

## General comments on paper (7/10):

* clear paper, one of the first and popular papers on the topic of Bayesian NNs

## Comments:

* very neat explanation of Bayesin Networks training: 
  1) reparametrization-trick 
  2) ELBO cost function
  3) ELBO gradient estimation via sampling 
  
* like idea from formula 9, that we could use different weights for prior part of 
ELBO and on average cost function will be valid

* section 4.1 explains such technique as Thompson sampling, but for me it
was not the most clear

* experiments section shows not the most impressive setups (like training 
on MNIST), maybe because on more complicated tasks it performs worse 
