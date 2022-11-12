# Gradient Descent Algorithm
Gradient descent is an optimization algorithm which is commonly-used to train machine learning models and neural networks.  Training data helps these models learn over time, and the cost function within gradient descent specifically acts as a barometer, gauging its accuracy with each iteration of parameter updates. Until the function is close to or equal to zero, the model will continue to adjust its parameters to yield the smallest possible error. Once machine learning models are optimized for accuracy, they can be powerful tools for artificial intelligence (AI) and computer science applications. 

## Table of Contents
+ [About](#about)
+ [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>
Purpose of this project is to demonstrate the practical implementation of how gradient descent algorithm works.

### Prerequisites

What things you need to install the software and how to install them.
- VSCode
- Python
- Numpy

### Installing
To install numpy library run the following command on terminal.

```
pip install numpy
```
# Contributing Guide

- Contributing to The Documentation Compendium is fairly easy. This document shows you how to get started

## General
- The [Codebase Structure](./CODEBASE_STRUCTURE.md) has detailed information about how the various files in this project are structured
- Please ensure that any changes you make are in accordance with the [Coding Guidelines](./CODING_GUIDELINES.md) of this repo

## Submitting changes

- Fork the repo
  - <https://github.com/pravinkori/Gradient-Descent.git>
- Check out a new branch based and name it to what you intend to do:
  - Example:
    ````
    $ git checkout -b BRANCH_NAME
    ````
    If you get an error, you may need to fetch fooBar first by using
    ````
    $ git remote update && git fetch
    ````
  - Use one branch per fix / feature
- Commit your changes
  - Please provide a git message that explains what you've done
  - Please make sure your commits follow the [conventions](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53#file-commit-message-guidelines-md)
  - Commit to the forked repository
  - Example:
    ````
    $ git commit -am 'Add some fooBar'
    ````
- Push to the branch
  - Example:
    ````
    $ git push origin BRANCH_NAME
    ````
- Make a pull request
  - Make sure you send the PR to the <code>fooBar</code> branch
  - Travis CI is watching you!

If you follow these instructions, your PR will land pretty safely in the main repo!
