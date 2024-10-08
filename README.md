# DB-Visual-Hackathon

# Overview - Solution to Prompt 2

## Tools Used

Participants are encouraged to use the following tools:
- Streamlit
- Python
- APIs for data

## Prompt 2: Visualization of Financial Statement

Quarterly financial data on publicly traded companies can take a long time to manually retrieve (especially for long stretches of time). Financial statements can also be very dense. Since they are packed with a lot of information, we want to narrow down the visualization to a few key-metrics. If we input a company ticker, we should be able to retrieve quarterly data from the following-key-metrics: 
  1. Company's name
  2. Company's mission statement (if available)
  3. Qualitative description of what the company does
  4. Revenue Per Share
  5. Net Income Per Share
  6. Free Cash Flow Per Share
  7. Tangible Book Value Per Share


### Visualization of Financial Statement

**Objective:** Create a visualization tool for key financial metrics of publicly traded companies.

**Key Features:**
- Retrieve quarterly financial data based on company ticker
- Display the following key metrics:
  1. Company's name
  2. Company's mission statement (if available)
  3. Qualitative description of what the company does
  4. Revenue Per Share
  5. Net Income Per Share
  6. Free Cash Flow Per Share
  7. Tangible Book Value Per Share

## Instructions

The objective of this hackathon is to create at minimum a proof of concept (POC), or at best a working Minimum Viable Product (MVP) for your team's selected prompt. Teams can utilize datasets from any open-source platform with the challenge to present a detailed outline of your concept or testable model aligning to your chosen prompt.

## Hackathon Rubric

1. **Prompt Accuracy:** Alignment to Prompt Guidelines
2. **Presentation:** Oral Delivery
3. **Originality:** "Outside the box" thinking for concepts, design, and name
4. **Technical Acumen:** SDLC principles, code maintainability, and use of right technology for the appropriate application
5. **Usability:** Augmented for future use, Accessibility, Exhibits concepts DB values

## SDLC Principles:

- Follow Agile methodologies for iterative development
- Implement version control using Git
- Conduct regular code reviews
- Practice continuous integration and continuous deployment (CI/CD)
- Prioritize code quality and maintainability
- Implement error handling and logging
- Ensure scalability and performance optimization

## Best Practices:

### Documentation:
- Maintain clear and up-to-date README files
- Use inline comments for complex code sections
- Generate API documentation using tools like Sphinx or Doxygen
- Create user guides and technical documentation
- Document design decisions and architecture

### Unit Testing:
- Write unit tests for all new features and bug fixes
- Aim for high test coverage (e.g., 80% or higher)
- Use testing frameworks like pytest for Python
- Implement mock objects and fixtures for isolated testing
- Run tests automatically as part of the CI/CD pipeline

### GitHub Actions:
- Set up automated workflows for CI/CD
- Configure linting and code style checks
- Automate unit test execution on pull requests
- Implement security scanning for vulnerabilities
- Set up automatic deployment to staging/production environments

## CI/CD Pipeline

We use GitHub Actions to implement our CI/CD pipeline. This automates our build, test, and deployment processes, ensuring code quality and faster development cycles.

### Workflow Overview

Our CI/CD pipeline consists of the following steps:

1. **Build and Test**: Triggered on every push and pull request to the `main` branch.
   - Sets up the Python environment
   - Installs dependencies
   - Runs unit tests
   - Performs linting

2. **Deploy**: Triggered only on pushes to the `main` branch after successful build and test.
   - Deploys the application to our production environment

### Setting Up GitHub Actions

To contribute to this project and work with our CI/CD pipeline:

1. Fork the repository
2. Clone your forked repository locally
3. Create a new branch for your feature or bug fix
4. Make your changes and commit them
5. Push your branch to your fork
6. Create a pull request to the main repository

The CI/CD pipeline will automatically run on your pull request, checking for any issues before merging.

### Automatic Pull Requests

To streamline our workflow, we encourage the use of automatic pull requests. Here's how to set it up:

1. Install the [GitHub CLI](https://cli.github.com/) tool
2. Authenticate with your GitHub account: `gh auth login`
3. Use the following command to create a pull request automatically:

   ```bash
   gh pr create --base main --head your-branch-name --title "Your PR Title" --body "Description of your changes"
   ```

This command will create a pull request from your current branch to the `main` branch of the original repository.

### Best Practices for Working with CI/CD

- Always create a new branch for your work
- Keep your branches up to date with the main repository
- Write meaningful commit messages
- Ensure all tests pass locally before pushing
- Address any issues flagged by the CI/CD pipeline promptly

## Contributing:

- Fork the repository and create a new branch for your feature or bug fix
- Follow the coding style and conventions used in the project
- Write clear commit messages and keep commits atomic
- Create a pull request with a detailed description of your changes
- Ensure all tests pass and add new tests if necessary
- Respond to code review comments and make requested changes

# License:

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
