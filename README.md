Documentation for Running, Testing, and Deploying the Service

1. Running the Service Locally

Prerequisites
•	Python 3.9 or later
•	Pip package manager
•	Virtual environment (recommended)
•	.env file containing the necessary API keys and environment variables


Steps to Run Locally
1.	Clone the repository:
2.	git clone <repository-url>
        cd <repository-folder>
3.	Set up a virtual environment:
4.	python -m venv venv
        source venv/bin/activate  
        On Windows: venv\Scripts\activate
5.	Install dependencies:
        pip install -r requirements.txt
6.	Create a .env file in the root directory and add the following variables:
        API_KEY=<your_paystack_api_key>
7.	Run the service:
        flask run
        The service will be available at http://127.0.0.1:5000.
8.	Testing the API:
        o	Use a tool like Postman to test the endpoints.
        o	Include headers such as authentication and content type when making requests



2. Understanding the Tests

Test Setup
Tests are written using pytest. Ensure all dependencies are installed and the service is properly configured.

Steps to Run Tests
1.	Ensure the service dependencies are installed (if not already done):
        pip install -r requirements.txt
2.	Run the tests:
        pytest
3.	View Test Results:
        o	Upon running pytest, the output will display details about which tests passed, failed, or were skipped.

Key Tests
1.	test_payment_status:
        o	Tests the POST /api/v1/payments endpoint for creating a payment and validates the status.
2.	test_payment_retrieval:
        o	Tests the GET /api/v1/payments/<payment_id> endpoint for retrieving the status of a payment.



3. Deploying Using the CI/CD Pipeline

The pipeline is configured to:
•	Automatically run tests and ensure code quality.
•	Deploy the application to Render whenever new code is pushed to the master branch.


Prerequisites
1.	GitHub Repository: Ensure your Flask application's codebase is hosted on GitHub.

2.	Render Account: Set up an account on Render.

3.	Render API Key: Obtain your Render API Key from your Render dashboard.

4.	GitHub Secrets: Add your Render API Key and other sensitive information as GitHub secrets.


Setting up the GitHub Workflow
The following GitHub Actions workflow file is designed to:
1.	Install dependencies.
2.	Create a .env file using GitHub secrets.
3.	Run tests with pytest.
4.	Automatically deploy the application to Render upon successful tests.

