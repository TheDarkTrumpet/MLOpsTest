# cat-toy

## Purpose

This directory is intended for my presentation on Wednesday, 8/3/2022.  So the files here are intended to be described. 
The script below is what I plan to go over in my presentation, so even without it, you can potentially follow along.

## Model Preparation

1. Look at the `generateData.ipynb` file, we're generating fixture data for this story about my cat.
2. Running the entire notebook start to finish will generate a new data file (/data/cat-happiness.csv)

## Model Investigation and Testing

1. Look at the /weka/* files.  Ran Weka first with the CSV, looked at the features and looked at what's important for the target.
2. Tried various models, automated fashion, to determine the best model that would fit the data set.
3. Tested a few models on my own, verifying the algorithm's results, too.

## Model Generation (through code)

1. Starting with `mlInteractive.ipynb`, we're generating a few models using sklearn.
   - KNN = K-Nearest Neighbors
   - Random Forest
2. Running through `mlInteractive.ipynb` will generate a model, called `cat_toy` with a hash.
   - Concept of 'latest', just like Git
   - The hashes are also useful, but don't really have a relationship with each other (so not like Git)
   - Models stored in: `$HOME/bentoml/models/cat_toy/<HASH>`

## Model Loading (through code)

1. Look at `mlInteractive-SavedModel.ipynb`
2. We load the `cat_toy:latest` model, and can pass an ndarray to it to get the prediction

## Generating a Service

1. Open `service.py`
   - Defines the various APIs we can create.  There are two here.
   - Note we have two APIs defined, but will go over that later.
2. Open `bentofile.yaml`
   - This is very similar to that of a Docker file, it's a definition file of how our service is built.
3. In terminal, cd to the directory and run `bentoml serve`
4. Go to http://127.0.0.1:3000
   - Show web browser, and the two endpoints.
   - For endpoint 1 (classify).  Click 'Try it Out' and use the response body: [[0, 1, 0, 0, 1, 0]]
   - For endpoint 2 (jclassify). Simply run without input.