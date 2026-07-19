# Notes

## How to run

1. Install uv 
`curl -LsSf https://astral.sh/uv/install.sh | sh`

2. Sync the environment `uv sync`

3. Execute the tests `uv run pytest`

Optional:

`uv run mypy` type checking (for src and also for tests)

`uv run ruff check` linting

`uv run ruff check --fix` autofix linting problems

`uv run ruff format` formatting

## Use of AI

The use of AI in this project is strictly limited to boost my python learning process. I use the claude desktop app with my pro subscription to ask questions and learn more about python ecosystem (package managers, test frameworks/utils, standard library apis...), syntax, types and similar things.

In my opinion this is one of the most legitimate uses of ai, and a very effective one if you complement it with a different source of thruth. During the past 6 years I have developed a strong mastery of nodejs, and something I have realised is that when you truly master something you are then able to get the most of ai. You have adquired judgement to know what is good and what not, being able to steer the ai.

Long story short, if you only study using ai and at the same time delegate most of the coding to it, you will never reach mastery, thus not having the neccessary judgement you need.

## Why I chose python

I could have chosen nodejs with typescript to move faster and be more confortable, but I don't think that would show what actually matters for this role. 

On one hand I would like to show that I can get out of my confort zone and I can pick up a new stack. On the other hand, whoever reviews this probably works in python, so using node would force to make an extra effort to understand the solution. My backend experience is transferable, the concepts are the same.

## Tooling decisions

- **uv:** Written in Rust (super fast), provides package management isolation with lock file and python versioning. I found it makes python development very similar with nodejs with npm, surprising.
- **pytest:** After some investigation it seems to be the most used library to write tests and provides defaults like parametrization and syntax very similar to nodejs test runner.
- **mypy:** Code types.
- **ruff:** Linter and formatter.
- **httpx**: I searched for a http library with async support, as the requirements of the project say we have to call and api, although in practice we are going to mock it so it's a bit useless.

## Design decisions

- As the requirements of the project said, we don't need to implement an http api nor a cli app, so I will just expose the app though __init__.py, without a main file. We can observe how the program behaves running the test suite.
- Use a TDD approach with BDD test names, I will develop the solution outside in using tdd, the acceptance test will drive my development.
- For good testing practices I usually follow the approach of coding by hand my own test doubles, I love this guide about test doubles from Fran Iglesias https://franiglesias.github.io/test-doubles-1/ https://franiglesias.github.io/test-doubles-2/ I even participated in a kata with him.
- I suppose samples will always contain 1 and 0 as values, so i don't add a defensive programming line to check if the value is allowed (-1, 5, 9)...
- In contiguous_ones the spec says: "counts each 1 that is next (but not previous) to another 1 as a positive cell", but it was more intuitive for me to think about it like "counts each 1 that has a previous 1 as a positive cell".