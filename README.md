# FlowCleanser

## Description
FlowCleanser is a command-line tool designed for the deletion of GitHub Actions workflow runs in a specified repository. This tool is particularly useful for automating the clean-up of old or unnecessary workflow runs, aiding in resource management and organization of your GitHub projects.

## Installation

To install FlowCleanser, follow these steps:

1. Clone the repository:
   ```
   git clone git@github.com:MishchenkoDaniil/FlowCleanser.git
   ```
2. Navigate to the project directory:
   ```
   cd flowcleanser
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use FlowCleanser, execute the script with the necessary parameters:

```
python main.py -o <owner> -r <repository> -t <token>
```

Where:
- `<owner>` is the GitHub repository owner.
- `<repository>` is the name of the repository.
- `<token>` is your GitHub token for authentication.

## License

GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please feel free to contact me at dany.mishchenko@gmail.com.

---
© 2024 Daniil Mishchenko, FlowCleanser