name: CI on Push

on:
  push:
    branches:
      - main
      - 'feature/*' # Triggers on any branch that starts with 'feature/'

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14' # Specify your Node.js version

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test
