name: Build and Deployss

on:
  push:
    branches:
      - feature

        
jobs:
  build_and_deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2
          
      - name: Use metadata from api
        run: |
          echo "Branch: ${{ github.event.inputs.changed_files }}"
