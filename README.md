# aws-cloudresume-backend


# 🌐 Cloud Resume Challenge Visitor Counter

This repository showcases the implementation of a **serverless visitor counter** using AWS Lambda, API Gateway, DynamoDB, and frontend JavaScript as part of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/).

## 🚀 Features

✅ Visitor count displayed dynamically on a static site  
✅ **Lambda** function updates and returns the count from DynamoDB  
✅ **API Gateway** with CORS-enabled POST endpoint  
✅ Static site hosted via S3 and CloudFront  
✅ Automated CI/CD pipeline with GitHub Actions (optional)  
✅ **Infrastructure as Code** with Terraform (optional, not in this repo)

---

## ⚙️ Tech Stack
- **Frontend:** HTML/CSS, JavaScript (`fetch` API)
- **Backend:** AWS Lambda (Python), API Gateway
- **Database:** DynamoDB
- **DevOps:** AWS CloudFormation / Terraform (optional), GitHub Actions (optional)

---

## 💡 What We Did

- Built a static HTML/CSS site with a visitor counter (`<span id="visitor-count"></span>`).
- Developed a **Python Lambda function** to increment and fetch visitor counts from DynamoDB.
- Configured **API Gateway** as a proxy integration for Lambda, including:
  - **POST** endpoint for updating the count
  - **OPTIONS** method for CORS preflight requests
- Enabled **CORS headers** in:
  - API Gateway console (OPTIONS response)
  - Lambda function response headers (`Access-Control-Allow-Origin: *`)
- Deployed and tested using `curl` commands and browser console.

---

## 🪲 Errors Encountered & Fixes

- **Issue:** Visitor count did not load on custom domain (CORS error).  
  **Fix:**  
  - Confirmed **OPTIONS** preflight headers returned `Access-Control-Allow-Origin`.  
  - Verified the **Lambda** POST response also included `Access-Control-Allow-Origin: *`.

- **Issue:** Missing CORS headers in Lambda response.  
  **Fix:**  
  - Added explicit `headers` in `lambda_handler` response:
    ```python
    'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
    },
    ```

- **Issue:** Inconsistent count display.  
  **Fix:**  
  - Used `window.onload` in JS to ensure visitor count fetched after page load.

---

## 🚀 How to Deploy
1. Deploy **Lambda function** in AWS (Python runtime).  
2. Deploy **API Gateway** with POST and OPTIONS methods.  
3. Create DynamoDB table `VisitorCount` with primary key `id` = `"counter"`.  
4. Update **frontend HTML** with your API Gateway endpoint URL.  
5. Upload static site to S3 and configure CloudFront (for HTTPS).  
6. Enjoy dynamic visitor counts on your Cloud Resume!

---

## 📷 Screenshot

![visitor-counter-demo](./assets/visitor-counter-demo.png)

---

## 🔗 Live Demo
[https://yourdomain.com](https://yourdomain.com)

---

## 📬 Contact
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)  
- Email: yourname@example.com