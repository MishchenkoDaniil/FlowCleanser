# FlowCleanser

This script, created by Mishchenko Daniil, is designed to manage and clean up workflows in a specified GitHub repository. It allows users to delete runs of GitHub Actions workflows based on the provided repository and owner details.

## Prerequisites

Before using this script, ensure you have the following installed:
- `git`
- `curl`
- `jq`

## Installation

1. **Clone the repository:**

   ```bash
   git clone git@github.com:MishchenkoDaniil/FlowCleanser.git
   ```

2. **Navigate to the repository directory:**

   ```bash
   cd FlowCleanser
   ```

3. **Make the installer executable (if it's not already):**

   ```bash
   chmod +x install.sh
   ```

4. **Run the installer:**

   ```bash
   sudo /install.sh
   ```

## Usage

After installation, you can use the script by running it with the required flags:

```bash
flowcleanser -o <owner> -r <repo> -t <token>
```

Where:
- `<owner>` is the owner of the GitHub repository.
- `<repo>` is the repository name.
- `<token>` is your GitHub personal access token.

## Author

**Mishchenko Daniil**

Feel free to contact me for any feedback or questions regarding this script.
```
