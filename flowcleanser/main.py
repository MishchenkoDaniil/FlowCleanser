#!/usr/bin/env python3

import requests
import sys
import getopt

def delete_workflow_runs(owner, repo, token):
    # Base URL for GitHub API
    base_url = f"https://api.github.com/repos/{owner}/{repo}"

    # Headers for authorization and request
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    try:
        # Fetch workflows
        workflows_response = requests.get(f"{base_url}/actions/workflows", headers=headers)
        workflows_response.raise_for_status()  # Check for HTTP errors

        for workflow in workflows_response.json()['workflows']:
            print(f"Processing workflow: {workflow['name']} with ID {workflow['id']}")

            # Fetch runs for each workflow
            runs_response = requests.get(f"{base_url}/actions/workflows/{workflow['id']}/runs", headers=headers)
            runs_response.raise_for_status()  # Check for HTTP errors

            # Delete each run
            for run in runs_response.json()['workflow_runs']:
                delete_response = requests.delete(f"{base_url}/actions/runs/{run['id']}", headers=headers)
                if delete_response.status_code == 204:
                    print(f"Successfully deleted run {run['id']}.")
                else:
                    print(f"Failed to delete run {run['id']}.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def main():
    owner = ''
    repo = ''
    token = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], "o:r:t:", ["owner=", "repo=", "token="])
    except getopt.GetoptError:
        print('Usage: flowcleanser -o <owner> -r <repo> -t <token>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-o", "--owner"):
            owner = arg
        elif opt in ("-r", "--repo"):
            repo = arg
        elif opt in ("-t", "--token"):
            token = arg

    if not all([owner, repo, token]):
        print('Usage: flowcleanser -o <owner> -r <repo> -t <token>')
        sys.exit(2)

    delete_workflow_runs(owner, repo, token)

if __name__ == "__main__":
    main()
