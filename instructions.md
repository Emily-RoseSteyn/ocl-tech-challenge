# tech-challenge
Short tech challenge for candidates applying to Open Cities Lab

# Tech Assessment

## Instructions
- All code and your response should be on a public GitHub repository.
- Share the GitHub repository link with wasim@opencitieslab.org.

## Part 1: Web Scraping and Data Storage

Write a Python script to:

1. Scrape data from the following options on [Valuation 2022 Durban](https://valuation2022.durban.gov.za/):
   - Full Title Property
   - Sectional Title Property
2. Clean the scraped data to ensure consistency and accuracy.
2. Store the scraped data in a PostgreSQL database.

## Part 2: API Development [https://swagger.io/docs/specification/about/]

Create a GET API to query the data stored in Part 1 using the OpenAPI specification. Ensure the API includes:

1. The schema for both the request and response objects.
2. The OpenAPI specification attached to the repository.

## Part 3: Deployment Strategy

Write a short solution outlining how you would deploy this application to production. Your solution should address the following:

1. How to schedule the scrapers to run daily and save the data to the database.
2. Which Python web application framework you would use to deploy the API from Part 2 and what the deployment would look like on your chosen cloud provider. Include details such as the architecture, services used, and any relevant configurations.
3. How you would handle errors, downtime & alerts. 

## Submission

Please ensure all parts of the assessment are completed and included in this repository. Once done, share the link to the repository with wasim@opencitieslab.org.

Should [Valuation 2022 Durban](https://valuation2022.durban.gov.za/) not be working use [Valuation 2012 Durban](https://valuation2012.durban.gov.za/) or [Valuation 2017 Durban](https://valuation2017.durban.gov.za/)
