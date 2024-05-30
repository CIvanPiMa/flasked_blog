# Flasked Blog

Blog style website developed on flask styled with bootstrap

- [Docs](https://civanpima.github.io/flasked_blog/flasked_blog.html).

## Installation

```shell
pip install flasked_blog
```

## Usage

...TBD

## Contributing

Once cloned the repo, install the [pre-commit](https://pre-commit.com/#install) hooks:

```shell
pre-commit install --install-hooks --hook-type commit-msg
```

Install the library (in a virtual environment) as an editable package with the development dependencies:

```shell
pip install -e ".[dev]"
```

### Documentation

- This library uses the [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html) format for the docstrings.
- To generate the documentation, run:

```shell
pdoc src/flasked_blog --mermaid --docformat numpy
```

### Testing

To run the tests:

```shell
behave
```
