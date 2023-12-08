# Loan Application System

Thank you for the coding assessment opportunity. I've included some additional elements in the code for demonstration purposes. Looking forward to your feedback.. Cheers.

## Overview
This repository contains the code for a Loan Application System. The system is built using Python 3.11/Flask for the backend and React for the frontend. It allows users to submit loan applications and receive pre-assessment results.

## Features
- Users can enter their business details, including name, year established, loan amount, and accounting provider.
- The system fetches a balance sheet for the last 12 months based on the accounting provider.
- Pre-assessment results are calculated based on profit/loss and assets value.
- Results are displayed on the frontend.

## Prerequisites

- Python 3.11
- Node 18
- Docker

## Running the Application via Docker

1. `docker compose up` will start all the required services
2. `docker compose down` will shutdown all containers
3. Access the application in your web browser at `http://localhost:3000`

## Running Tests

1. `pytest testing/` will run all tests for backend
2. `cd /frontend && npx cypress run` will run all e2e tests
3. `npx cypress open` if you like to run them on UI

## Installation
1. Clone the repository: `git clone https://github.com/yourusername/loan-application-system.git`
2. Install backend dependencies: `cd backend && pip install -r requirements.txt`
3. Install frontend dependencies: `cd frontend && npm install`

## Usage
1. Start the backend server: `cd backend && flask run`
2. Start the frontend development server: `cd frontend && npm start`
3. Access the application in your web browser at `http://localhost:3000`