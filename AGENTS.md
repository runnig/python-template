# Project Context: python-template

## Project Overview

This is a basic Python project template.
It provides a simple structure for a Python application, including source code, tests, and dependency management.

The project uses
* `uv` for managing dependencies, as indicated by the `uv.lock` file,
* `pytest` for running tests.
* The main application logic resides in the `src` directory, with a sample `main.py` entrypoint and an `arithm.py` module containing a simple `sum` function.

The project is configured to use Python version 3.12, specified in the `.python-version` file.

## Project structure

The project uses `uv workspaces` to manage modules. Read more about
uv workspaces: https://docs.astral.sh/uv/concepts/projects/workspaces/

The modules are added to "packages/" and have their own pyproject.toml
For example, module "arithm" would be located at "packages/arithm".
Source code goes to "src" subdirectory, unit-tests tests go to "tests" subdirectory:

```bash
$ tree packages/arithm
packages/arithm
├── pyproject.toml
├── src
│   └── arithm
│       ├── __init__.py
│       └── arithm.py
└── tests
    └── test_arithm.py
```

## Module anatomy

The concrete function signatures and implementations go to
"packages/modulename/src/modulename/modulename.py"

The publicly callable functions should be added to the `__all__` list
in `__init__.py`

Example:
```py
# file: packages/arithm/src/arithm/arithm.py
# concrete implementation

def my_func(a: int, b: int) -> int:
    """This function is a part of public API of the module arithm."""
    return a + b

# file: packages/arithm/src/arithm/__init__.py
# public API
from arithm.arithm import my_func

# Add the publicly callable functions of the module to the `__all__` list:
__all__ = ["my_func"]

# file: packages/arithm/tests/test_arithm.py
# unit-tests
import arithm

def test_my_func() -> None:
    a = 1
    b = 2
    assert arithm.my_func(a, b) == 3

```

## Main Commands

* Before running any commands, make sure to activate the virtual environment:
  `source .venv/bin/activate`.
* Check that the virtual environment was activated:
  `echo $VIRTUAL_ENV`.
* Invoke the command `make test` in the terminal to run all tests.
* Alternatively, run pytest for each package, example:
   `uv run --exact --package arithm pytest packages/arithm`
* `make lint` to check all formatting.
* Alternatively, run ruff for each package, example:
  `uv run ruff check packages/arithm`

## Building and Running

## Install uv

https://docs.astral.sh/uv/getting-started/installation/

## Virtual Environment

Create a virtual environment if you don't have it yet.
It is a local directory that contains all installed dependencies:

```bash

uv venv

```

```
$ tree -L 1 .venv
.venv
├── bin
├── lib
├── lib64 -> lib
└── pyvenv.cfg
```

### Dependencies

Before running any commands, activate the virtual environment:
```bash
source .venv/bin/activate
```

Check if the virtual environment was activated correctly by running the command below.
If this command output is empty, then the virtual environment is not activated.

The `.venv` directory contains a Python virtual environment with all project dependencies installed. It's created using `uv` and should be activated before running any commands.

```bash
echo $VIRTUAL_ENV
```

Install a dependency, e.g. pandas:

```bash
uv add pydantic
uv sync
```

Install a tool:

```bash
uv tool install ruff
```

### Running the Application

The main entrypoint of the application can be run directly:

```bash
uv run python main.py
```

```bash
uv run python main.py
```

### Testing

The project uses `pytest` for testing.
Tests are located in the `tests/` directory.
Run the tests using the `Makefile` command:

```bash
make test
```

Alternatively, run individual unit-tests: `uv run pytest tests/path/to/test_module.py`.

To run a specific test function:
```bash
uv run pytest tests/path/to/test_module.py::test_function_name
```

## Development Conventions

*   **Source Code:** Application source code is located in the `src/` directory.
*   **Tests:** Tests are placed in the `tests/` directory.
    Test files should be named following the `test_*.py` convention.
    The unit-tests should mirror the main source code directory paths, e.g. for a module
    located at src/path/to/module.py, the corresponding unit-test should be located at
    tests/path/to/test_module.py
*   **Typing:** The code uses Python's type hints (e.g., `def sum(a: int, b: int) -> int:`).
    `mypy` is a dependency, static type checking is a must.
    Unit-tests must also be strongly typed, example signature: `def test_sum(fixture) -> None:`
*   **DO NOT USE MOCKS**: Avoid patches and MagicMock. Instead use "test doubles" pattern - see below.
*   **Pre-commit Hooks:** The presence of `pre-commit` in the dependencies suggests that there are pre-commit hooks configured to maintain code quality and consistency. You should install and configure pre-commit hooks for development.

## Workflow

* Make sure the virtual environment is activated
* After making code changes and before commits,
  check that the code has corresponding unit-tests.
  If not, create the unit-tests.
* Run the unit-tests for the changed source code
* Run `mypy` on the changed source code and on the tests.
* Finally run `make lint` to trigger the pre-commit checks
* If there are pytest/mypy/lint warnings or errors, make sure to fix them before
  commits

## Styleguide

* Use enum.StrEnum instead for known strings
* Use pydantic.BaseModel and dataclasses to express "data-only" structures.
* For each value in the dataclass/BaseModel add example values and/or valid value ranges.
* Use pydantic.BaseSettings to read the configuration from environment variables and from
  command line flags.
* Use pure Python module-level free functions instead of @staticmethods and @classmethods.
* Use Python modules extensively - see the "Good Module Example" below.
* Use inheritance where Liskov Principle is applicable: where a base/abstract interface will
  be redefined in the implementations.
  1. Define an abstract interface using typing.Protocol.
  2. Define implementations for no-op, tests and production
* Where possible, use empty strings and empty lists to signal missing or undefined values
  instead of using None
* Use dependency injection and factory patterns.
* Adhere to the SOLID principles:
  1. **Single Responsibility Principle (SRP)**: A class should have only one reason to change, meaning it should only have one job or responsibility.
  2. **Open/Closed Principle (OCP)**: Software entities should be open for extension but closed for modification.
  3. **Liskov Substitution Principle (LSP)**: Objects of a superclass shall be replaceable with objects of its subclasses without breaking the application.
  4. **Interface Segregation Principle (ISP)**: Clients should not be forced to depend on interfaces they don't use.
  5. **Dependency Inversion Principle (DIP)**: High-level modules should not depend on low-level modules. Both should depend on abstractions.

## Modules to use

* FastAPI for endpoints. Make sure to use async endpoints.
* uvicorn for web servers

## Good Module Example

Good example of a module with an illustration of Liskov principle,
good docstrings, field comments, enums

```python
# packages/mymodule/src/mymodule/myservice/models.py

class MyServiceRequest(pydantic.BaseModel):
  """Short doc string."""
  # example valid values: 1, 2, ..,  10
  int_value: int

  # valid range: [0, 1] inclusive
  float_value: float

class EnumExampleColor(enum.StrEnum):
  RED = "red"
  YELLOW = "yellow"
  UNDEFINED = "undefined"

class MyServiceResponse(pydantic.BaseModel):
  """Short doc string."""

  # color of the output
  color: EnumExampleColor

  # string name
  # Do not use None to signal missing values - use
  # empty strings instead
  name: str = ""

  # Do not use None - use empty lists instead
  list_value: list[str] = []

# packages/mymodule/src/mymodule/myservice/myservice.py
class MyService(typing.Protocol):
  """Short docstring."""
  def process(self, req: MyServiceRequest) -> MyServiceResponse:
    """Short docstring."""
    ... # no implementation in the abstract interface

class MyServiceNoop(MyService):
  """No-op implementation - does nothing."""
  def process(self, req: MyServiceRequest) -> MyServiceResponse:
    """Short docstring."""
    return MyServiceResponse(color=EnumExampleColor.UNDEFINED)

class MyServiceTest(MyService):
  """Unit-test implementation (test double) - returns ."""
  def __init__(self, resp: MyServiceResponse) -> None:
    self.resp = resp

  def process(self, req: MyServiceRequest) -> MyServiceResponse:
    """Short docstring."""
    return self.resp

class MyServiceProd(MyService):
  """Production implementation - calls the API."""
  def __init__(self, http_client: httpx.AsyncClient) -> None:
    self.http_client = http_client

  def process(self, req: MyServiceRequest) -> MyServiceResponse:
    """Calls the remote API."""
    # Real production implementation

# packages/mymodule/src/mymodule/myservice/factory.py

def make(env: environment.Environment, args: MyServiceArgs) -> MyService:
  match env:
    case environment.PROD:
      return MyServiceProd(cfg)
    case environment.UNIT_TESTS:
      return MyServiceTest(cfg)
    case environment.NOOP:
      return MyServiceNoop(cfg)

# packages/mymodule/src/mymodule/myservice/__init__.py

from path.to.myservice.models import (
  MyServiceRequest,
  MyServiceResponse,
)
from path.to.myservice.myservice import MyService
from path.to.myservice.factory import make

__all__ = [
  "MyService",
  "MyServiceRequest",
  "MyServiceResponse",
  "make",
]

# packages/mymodule/tests/mymodule/myservice/__init__.py
import pytest

# IMPORTANT: Use test doubles instead of mocks.
# Motivation: During big rewrites,
# mypy can point to type errors in the code with
# test doubles. But with mocks and patches, mypy
# and other type checkers are blind.
class MyServiceOtherTestDoubleRaises(MyService):
  def process(self, req: MyServiceRequest) -> MyServiceResponse:
    raise ServiceUnavailableError("simulating service failure")

@pytest.fixture
def my_service_failure() -> MyServiceOtherTestDoubleRaises:
  return MyServiceOtherTestDoubleRaises()

def test_service_failure(my_service_failure: MyServiceOtherTestDoubleRaises) -> None:
  # prepare the test
  with pytest.assert_raises(ServiceUnavailableError):
    my_service_failure.process(some_request)

```

## Best Practices

* Start mypy daemon to speed up type checking: `dmypy start`
* Use "ripgrep" (rg) to search files quickly
