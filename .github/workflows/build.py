name: Build and Deploy

on:
  push:
    branches:
      - feature
  workflow_dispatch:
    inputs:
      branch:
        description: 'Branch name'
        required: false
      commit:
        description: 'Commit SHA'
        required: false
      author:
        description: 'Author of the commit'
        required: false
      changed_files:
        description: 'changed files'
        required: false
        
jobs:
  build_and_deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
          
      - name: Use metadata from api
        run: |
          echo "Branch: ${{ github.event.inputs.changed_files }}"
