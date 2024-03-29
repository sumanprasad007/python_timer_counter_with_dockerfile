# Python Countdown Timer with Contaerization

This is a Python script that implements a countdown timer. The timer duration can be specified in seconds using an environment variable. If the environment variable is not set, the timer will default to 60 seconds.

Requirements
Docker
Dockerfile
Pytest
CricleCI

# CI/CD Pipeline Archtiecture using CircleCI

![image](https://user-images.githubusercontent.com/55047333/236610288-85498f63-6402-456f-8874-f29967e27867.png)

# **📍** Introduction:

In today's fast-paced software development landscape, automation and continuous integration are paramount. CircleCI, a popular cloud-based continuous integration and delivery platform, empowers developers to build, test, and deploy their applications with ease. In this blog post, we will explore how to use CircleCI to streamline your Python project's development workflow. We'll delve into the provided code snippet, highlighting its essential components and discussing the importance, functionality, cost, and simplicity of CircleCI.

## **📍 Why Choose CircleCI?**

CircleCI offers numerous benefits that make it an attractive choice for Python developers. Let's explore some of the key reasons to embrace this platform: CircleCI offers crucial functionality that greatly enhances the development process of Python projects:

1. **Automated Builds**: CircleCI automatically triggers builds whenever code changes are pushed to your repository or a pull request is opened, ensuring that your project is continuously built and tested. This helps identify issues early on and allows for faster feedback loops.
    
2. **Parallel Testing**: CircleCI allows you to parallelize your test suite, significantly reducing the time it takes to run tests. This feature is especially valuable for larger projects with extensive test suites, enabling faster feedback and quicker iterations.
    
3. **Integration with Version Control**: CircleCI integrates seamlessly with popular version control systems like Git, GitHub, and Bitbucket. This integration facilitates automatic triggering of builds upon code changes and provides insights into the commit or pull request that initiated the build. It helps maintain a clear audit trail and ensures that every change goes through the proper CI/CD process.
    
4. **Customizable Workflows**: CircleCI's workflows enable you to define complex pipelines that orchestrate multiple jobs. You can specify dependencies between jobs, control the order of execution, and parallelize tasks as needed. This flexibility allows you to create tailored build and deployment processes that suit your project's specific requirements.
    
5. **Artifact Management**: CircleCI allows you to store and manage build artifacts, such as binaries, test reports, and documentation. This feature ensures that you have a centralized location to access and share these artifacts, making it easier for team members to collaborate and review changes.
    
6. **Notifications and Collaboration**: CircleCI integrates with various communication tools like Slack, email, and chat platforms, enabling you to receive build status notifications and collaborate with your team effectively. Real-time notifications keep everyone informed about the build status, making it easier to identify and resolve issues promptly.
    
7. **Deployment and Orchestration**: CircleCI supports seamless integration with cloud providers and deployment platforms, such as AWS, Google Cloud Platform, and Kubernetes. This integration allows you to automate the deployment process, ensuring that your application is deployed consistently across different environments.
    

## **📍** The step-by-step setup for CircleCi:

Instructions for setting up and running CircleCI for the Python project we've been discussing.

## **🔹**GitHub Repository to follow along:

```plaintext
https://github.com/sumanprasad007/python_timer_counter_with_dockerfile.git 
```

![image](https://github.com/sumanprasad007/python_timer_counter_with_dockerfile/assets/55047333/f9dd08f7-8d31-45ff-826c-427e14955671)

## **🔹** Step 1: Create a CircleCI Account

First, you need to create a CircleCI account if you don't already have one. You can sign up for a free account on the CircleCI website using your GitHub or Bitbucket credentials.

![image](https://github.com/sumanprasad007/python_timer_counter_with_dockerfile/assets/55047333/dd887f12-e010-4b37-bd2a-eda68d47b6e4)

## **🔹** Step 2: Set up the Project

Once you've created your account, you'll need to add your Python project to CircleCI. To do this, navigate to your CircleCI dashboard and click on the "Add Projects" button in the left-hand menu.

Next, select the repository containing your Python project and click "Set Up Project" to begin the configuration process.

![image](https://github.com/sumanprasad007/python_timer_counter_with_dockerfile/assets/55047333/4306569f-fe80-4abb-bcc4-ad9bae6b7521)

## **🔹** Step 3: Configure the Project

After selecting your project, you'll need to create a configuration file for CircleCI to use during the build process. In this case, we'll be using the YAML code from the previous section to define a job called "build."

Copy the code into a new file named `.circleci/config.yml` in the root directory of your project. Save the file and commit it to your repository.

![image](https://github.com/sumanprasad007/python_timer_counter_with_dockerfile/assets/55047333/3b688615-1b78-4607-bc54-ea75cc12ee21)

## **🔹** Step 4: Run the Build

With the configuration file in place, CircleCI will automatically start building your Python project whenever changes are pushed to the repository. You can view the build logs in the CircleCI dashboard by clicking on the job name under the "Jobs" tab.

![image](https://github.com/sumanprasad007/python_timer_counter_with_dockerfile/assets/55047333/80454b65-a32e-47e4-975b-30e7e06f8a82)

### **⚜ Understanding the Code**

Let's dive into the provided code snippet and understand its components. This example demonstrates a simple Python project's build process:

```plaintext
version: 2.1
jobs:
  build:
    docker:
      - image: cimg/python:3.11

    steps:
      - checkout

      - run:
          name: Install dependencies
          command: pip install -r requirements.txt
      - run: python countdown_timer.py

workflows:
  version: 2
  build_and_test:
    jobs:
      - build
```

The code is written in YAML format and consists of two main sections: `jobs` and `workflows`.

![image](https://github.com/sumanprasad007/python_timer_counter_with_dockerfile/assets/55047333/5ead1f8f-304a-411b-be9e-755e63911d04)

### **⚜ Jobs**

Under the `jobs` section, we define a single job named `build`, which represents the build process for our Python project. It consists of the following steps:

1. **Docker Image**: We specify the Docker image `cimg/python:3.11` as the execution environment for our job. This image ensures consistency and reproducibility across different environments.
    
2. **Checkout**: The `checkout` step fetches the source code from the repository, allowing CircleCI to access and work with it.
    
3. **Install Dependencies**: This step installs the project's dependencies by running `pip install -r requirements.txt`. It ensures that all necessary packages are available for the project.
    
4. **Run Countdown Timer**: Here, we execute the Python script `countdown_timer.py`, which presumably contains code related to a countdown timer functionality.
    

### **⚜ Workflows**

The `workflows` section defines the execution flow and dependencies between jobs. In this case, we define a single workflow named `build_and_test` that contains one job, `build`. Workflows enable you to orchestrate multiple jobs and define their order of execution.

If everything is working correctly, you should see a "Success" message in the build logs. Congratulations, you've successfully set up CircleCI to build your Python project!

## **🔹** The following is the Dockerfile that can be used to build a Docker image for the countdown timer script:

FROM python:3.8-slim-buster

COPY countdown_timer.py /app/countdown_timer.py

WORKDIR /app

CMD ["python", "countdown_timer.py"]

# Execution Steps
Build the Docker image using the Dockerfile:

  docker build -t countdown_timer .
  
# Run the Docker container and specify the timer duration using the TIMER_SECONDS environment variable:

  docker run --name countdown_timer_container -e TIMER_SECONDS=<duration_in_seconds> countdown_timer
  
Replace <duration_in_seconds> with the desired timer duration in seconds.

The countdown timer will start running inside the container and will display the remaining time in the format mm:ss on the console, updating in real-time.

When the timer reaches 0, the message stop will be displayed.

## **🔹** Step 5: Add Tests

To further optimize your development process, you can also add automated tests to your CircleCI workflow. Simply uncomment the "Run tests" section in the configuration file, and add your tests to the project.

When you push changes to the repository, CircleCI will now run your tests as part of the build process, ensuring that your code is thoroughly validated before being deployed to production.

![image](https://github.com/sumanprasad007/python_timer_counter_with_dockerfile/assets/55047333/90a261a7-c6ec-44d5-9847-933a9e4cd20e)

# **📍Simplicity of CircleCI**

CircleCI's user-friendly interface and straightforward configuration make it easy to set up and integrate with your Python projects. Its YAML-based configuration file allows for a declarative approach to defining your build process, ensuring reproducibility and ease of maintenance.

CircleCI provides comprehensive documentation, tutorials, and example configurations to guide you through the setup process. Additionally, it offers a wide range of pre-built Docker images for popular programming languages, frameworks, and tools, simplifying the configuration of your build environment.

The platform's intuitive web interface provides real-time build logs, test results, and insights into the build status, making it easy to monitor and troubleshoot issues. CircleCI's focus on simplicity ensures that developers can quickly adopt and integrate it into their existing workflows without a steep learning curve.

## **📍 Cost and Free Credits**

CircleCI offers various pricing plans to accommodate different project sizes and requirements. It provides a free tier, which is suitable for personal projects or small teams getting started with continuous integration. The free tier typically includes a limited number of build minutes i.e. 6000 minutes per month and concurrent jobs. For larger projects or teams requiring more resources, CircleCI offers paid plans with increased build minutes, parallelism, and additional features. The pricing is usually based on factors such as the number of users, concurrent jobs, and additional add-ons or support options.

It's important to review the CircleCI pricing page ([**https://circleci.com/pricing**](https://circleci.com/pricing)) for the most up-to-date information on costs and available plans.
![image](https://github.com/sumanprasad007/python_timer_counter_with_dockerfile/assets/55047333/77735464-0a6f-4952-bc8a-eb97f66ac8ec)

# **📍** Conclusion:

In this blog post, we have explored how to use CircleCI to build Python projects. We started by understanding the provided code snippet, which demonstrates a basic CircleCI configuration for a Python project. We examined the YAML code, which defines a job named "build" that utilizes a Docker image, installs dependencies, and runs a Python script. CircleCI is a powerful and user-friendly platform for automating the build, test, and deployment processes of Python projects. Its integration capabilities, scalability, and extensive feature set make it an essential tool for modern software development teams. By leveraging CircleCI, you can streamline your development workflow, increase productivity, and deliver high-quality software more efficiently.

