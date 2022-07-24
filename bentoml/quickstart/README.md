# Quickstart

# Introduction

The code for this was taken from the BentoML QuickStart guide.  Not really intended for more than a a demo.

The readme is required for the bentofile.yaml directly

This file likely will contain my notes, too.

# Script and Run Order

## Develop Model

Start with the `quickstart.ipynb`.  Created an IRIS model and saved it.

The default location for this is in the home directory, `~/bentoml/models/iris_clf/`

They can be listed by running `bentoml models list`

## Create Service

The file `quickstart-service.py` is used to define an API service, but also to create the `bento` as well.

This can can be run, like in Development mode, by running:

`bentoml serve quickstart-service:svc --reload`

