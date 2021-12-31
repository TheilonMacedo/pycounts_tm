# pycounts_tm

A package to count the number of words in a text.  
This package is the result of my studies about how to create a documented and tested python package.

## Installation

```bash
$ pip install pycounts_tm
```

## Usage

# pycounts

Calculate word counts in a text file!

## Installation

```bash
$ pip install pycounts_tm
```

## Usage

`pycounts_tm` can be used to count words in a text file and plot results
as follows:

```python
from pycounts_tm.pycounts_tm import count_words
from pycounts_tm.plot_words import plot_words
import matplotlib.pyplot as plt

file_path = "test.txt"  # path to your file
counts = count_words(file_path)
fig = plot_words(counts, n=10)
plt.show()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. 
Please note that this project is released with a Code of Conduct. 
By contributing to this project, you agree to abide by its terms.

## License

`pycounts_tm` was created by Tomas Beuzen. It is licensed under the terms
of the MIT license.

## Credits

`pycounts_tm` was created with 
[`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and 
the `py-pkgs-cookiecutter` 
[template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pycounts_tm` was created by Theilon Macedo. It is licensed under the terms of the MIT license.

## Credits

`pycounts_tm` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
