# Mission Dotlas 🌎

[![Python version](https://img.shields.io/badge/python-v3.9-blue)](https://img.shields.io/badge/python-v3.9-blue)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/mission_dotlas/CONTRIBUTING.md)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-purple.svg)](https://opensource.org/licenses/BSD-3-Clause)

![Anaconda](https://img.shields.io/badge/Anaconda-44A833.svg?style=for-the-badge&logo=Anaconda&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

Part-Time Data Engineer Assessment

- [Mission Dotlas 🌎](#mission-dotlas-)
  - [Overview](#overview)
    - [About us](#about-us)
    - [The Mission](#the-mission)
  - [Getting started](#getting-started)
    - [Create a Private fork](#create-a-private-fork)
    - [Install Python `v3.9` or higher](#install-python-v39-or-higher)
    - [Install dependencies](#install-dependencies)
    - [Get crackin'](#get-crackin)
    - [Learning resources](#learning-resources)
  - [Evaluation](#evaluation)
    - [Submission](#submission)
    - [Criteria](#criteria)
    - [Nice-to-have](#nice-to-have)
    - [Contact](#contact)

> **Warning**
>
> **Applicants will be disqualified if they make a public fork of this repository.**
> Create a [private fork](#create-a-private-fork) instead.

## Overview

### About us

We at [Dotlas](https://dotlas.com) are building a suite of products for controlling, optimizing & growing retail businesses through AI-driven insights.

### The Mission

Your mission, should you choose to accept it, is to transform, process and analyze our dataset of **Restaurants in The State of California, USA**. Here are a few maps to get you inspired!

<p align="center">
  <img height="400" src="./assets/maps/california_restaurants.png" alt="Restaurants in California" />
  <p align="center">Restaurants in California</p>
</p>

<p align="center">
  <img height="400" src="./assets/maps/la_price_ranges.png" alt="Restaurants in Los Angeles, grouped into Hexagons according to their Price Range" />
  <p align="center">Restaurants in Los Angeles, grouped into <a href="https://www.youtube.com/watch?v=thOifuHs6eY">Hexagons</a> according to their Price Range</p>
</p>

<p align="center">
  <img height="400" src="./assets/maps/la_restaurant_density.png" alt="Restaurants in Los Angeles, on a Grid, height indicates count" />
  <p align="center">Restaurants in Los Angeles, on a Grid, height indicates count</p>
</p>

<p align="center">
  <img height="400" src="./assets/maps/sf_dress_code.png" alt="Restaurants in San Francisco, according to their Dress Code, height indicates count" />
  <p align="center">Restaurants in San Francisco, according to their Dress Code, height indicates count</p>
</p>

<p align="center">
  <strong>We&#39;ve uploaded our dataset to an
    <a href="https://studio.foursquare.com/public/5b812aeb-8e2b-4530-bbca-ca14429bf03e">interactive map</a>
   on Foursquare Studio. Feel free to explore it.
  </strong>
</p>

<p align="center">
  <img src="https://media0.giphy.com/media/3owzW2gwRKOG68Xu4E/giphy-downsized.gif?cid=6104955ec91oi7atpb4ge6dcogeal6fip5bwyqqgcz8e055y&rid=giphy-downsized.gif&ct=g" alt="Star Wars Map" />
</p>

## Getting started

### Create a Private fork

Let's create a private fork of this repository:

- [Go to the Import a repository page on GitHub](https://github.com/new/import)
- Fill in the information as shown below:

  <p align="center">
    <img height="400" src="./assets/private_fork.png" alt="How to create a private fork" />
    <p align="center">How to create a private fork</p>
  </p>

Once the repository is created on GitHub, clone it onto your local system!

### Install Python `v3.9` or higher

- You can download it from the [Python website](https://www.python.org/downloads/release/python-3105/)
- Or, you can install [Anaconda](https://www.anaconda.com/) and run the following command in your terminal:

  ```bash
  conda create --name dotlas python=3.9 -y
  conda activate dotlas
  ```

### Install dependencies

```bash
python -m pip install -r requirements
```

> You may install any additional dependencies!

### Get crackin'

Your mission's details are displayed in [mission.ipynb](./mission.ipynb).

### Learning resources

Please refer to [HELP.md](./HELP.md) for some resources to help you get acquainted with the tools you will need.

## Evaluation

### Submission

Once you're ready for evaluation, [invite us](#contact) as [private collaborators to your private fork](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)!

### Criteria

Submissions will be judged on:

- Readability & maintainability of code
- Correctness & approach to the solution
- Use of "best practices" by adhering to the [Pythonic way](https://towardsdatascience.com/how-to-be-pythonic-and-why-you-should-care-188d63a5037e)

### Nice-to-have

> Incorporating the following will be marginally helpful to the graders to reduce friction in evaluating your assignment

- Do not create additional branches on your private repository with the submission. Keep all changes on the `main` branch.
- Add your answers to the same file `mission.ipynb`
- Do not delete markdown sections of `mission.ipynb`. Feel free to add as many sections for documentation or otherwise as you need but don't delete sections already present.

### Contact

Feel free to reach out to us, should you have any questions.

| Name            | LinkedIn                               | GitHub                            |
| :-------------- | :------------------------------------- | :-------------------------------- |
| Nuno Freitas  | <https://www.linkedin.com/in/nunoamaralfreitas/> | <https://github.com/NaFreitaz>  |
| Eshwaran Venkat | <https://linkedin.com/in/eshwaranv98/>   | <https://github.com/cricksmaidiene> |
| Kelvin DeCosta  | <https://linkedin.com/in/kelvindecosta/> | <https://github.com/kelvindecosta>  |

> Feel free to ping us anytime for support.

<p align="center">
  <img src="https://media3.giphy.com/media/rHR8qP1mC5V3G/giphy.gif?cid=6104955e5o2xk6gadzs2yw1nignfpkhtg8bo08fm37d9sj6m&rid=giphy.gif&ct=g" alt="Students copying" />
  <p align="center"><strong>May the Force be with You!</strong></p>
</p>
