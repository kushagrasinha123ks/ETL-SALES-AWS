# ETL Sales Data with AWS

## Overview

Automated Sales Data Pipeline with AWS
- Developed a web portal using Python Flask that supports file uploads (CSV/Excel) up to 50 MB to AWS S3, utilizing the Boto3 AWS SDK for seamless integration.
- Designed and implemented an ETL pipeline with AWS Glue to transform and filter data using SQL queries, focusing on extracting information relevant to the Asian market.
- Efficiently managed data storage and retrieval by storing transformed data back in S3, facilitating easier analysis and reporting.


## Project Structure

- `createS3.py`: Script to create an S3 bucket and upload transformed data.
- `data.csv`: Sample sales data for ETL processing.
- `index.html`: HTML file for web interface.
- `requirements.txt`: Python dependencies for the project.
- `salesfavicon.png`: Favicon for the web interface.
- `style.css`: CSS file for styling the web interface.
- `upload.py`: Script to handle data upload to AWS S3.
- `script.py`: Script to handle data upload to AWS S3.

## Prerequisites

- Python 3.x
- AWS CLI (configured with your AWS credentials) or create .env file with AWS credentials
- Virtual environment tool (e.g., `venv`, `virtualenv`)

## MIT License

Copyright (c) 2024 Kushagra Sinha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

