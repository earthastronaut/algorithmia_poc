# algorithma_poc

Proof of concept for Algorithmia.

Source for https://algorithmia.com/algorithms/earthastronaut/poc


# POC Results

Algorithmia appears to provide an API Gateway and with an endpoint that you can
send data to in order to run a function (similar to OpenFaas).They manage versioning
of the published functions. They also provide a CLI tool for triggering functions
as well as managing data sources between your local and remote machine. 

Other features: managing compute resources, ability to make money based on endpoint usage (pass charged through), 

## What I Liked:

* Uses a repository to store your code and builds from that.
* Does make the endpoint creation easy.
* Automatic versioning of builds is nice.

## Functionality is easy to replicate

I wrote a simple flask app which can run and host the python function. Then we would
just need to host it on k8s, expose the port, and put it behind our own API gateway. 
Definitely more work for us but not much more. 

## No/Weak Secrets Managment

Though I did not go digging, there did not appear to be an easy secrets manager. 

## No Model Artifacts or Repository

Does not appear to be any way to package up models and store them. That must be built. 

## Local Dev is Needed

It appears that doing development locally is still needed. To keep enviornments portable
that would mean running Docker which then Algorithmia does not make easy to deploy. 

## Image Dependencies are not flexible

I caused a failure to build when I required `psycopy2` as a library. This library
requires that a C-lib is installed which needs to be done in addition. 

## No IDE for self hosted

Algorithmia uses a repo to store your code and provides two options: managed and self hosted.
For the self hosted, there does not appear to be any web IDE for interacting with the code
like there is for the managed. Not sure why. But it drives you even more to do local dev.

## Lacking MLOps Features

* No Hyperparameter Tuning: No way to test out different models or hyperparameters for models
from their interface. Would be nice to have something that could try out several
sets of hyperparameters for an endpoint and produce the results.

* No Pipelining: ML often requires a pipeline (example from kubeflow https://www.kubeflow.org/docs/images/pipelines-xgboost-graph.png) but this is not available.

* Weak Performance Metrics: No easy way to compare metrics across different builds. They 
do have an "insights" feature which does let you have some metrics so it's ...possible. 
Also does not appear to be a way to store image artifacts for a particular model+params+data.
