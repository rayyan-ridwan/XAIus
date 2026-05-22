# XAIus

> An explainable AI model selector for choosing ML approaches by transparency, interpretability, and salience.

## What it does

XAIus is a lightweight Python project for ranking candidate models by explainability signals and use-case fit.

## Why this project exists

- Make model selection more transparent
- Favor simpler, more explainable candidates when possible
- Keep the initial implementation small and easy to extend

## Project structure

```text
XAIus/
├── examples/
│   └── basic_usage.py
├── tests/
│   └── test_selector.py
├── xaius/
│   ├── __init__.py
│   ├── models.py
│   └── selector.py
├── README.md
├── requirements.txt
└── LICENSE
```

## Quick start

1. Clone the repository.
2. Use Python 3.11+.
3. Run the test suite:

```bash
python -m unittest discover -s tests
```

4. Try the example:

```bash
python -m examples.basic_usage
```

## Current development direction

- Expand the selector scoring strategy
- Add richer model metadata
- Introduce dataset- or domain-aware recommendations
- Add a small CLI for interactive exploration

## Contributing

Keep changes small, testable, and explainable. Add tests for any new selector behavior.
