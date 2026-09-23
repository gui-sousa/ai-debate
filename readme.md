# AI-Debate: Autonomous LLM Debate Orchestration with LangGraph 



<a name="readme-top"></a>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is a multi-agent debate platform built using **LangGraph** and **LangChain** to orchestrate autonomous interactions between two Large Language Models (LLMs) with opposing personas.

It addresses a fundamental architectural challenge in multi-agent conversational systems: **bypassing the strict role alternation constraints (`User` > `Assistant`) imposed by LLM provider APIs**.

### The Technical Challenge: Bypassing API Role Restrictions
Standard LLM APIs (e.g., OpenAI, Anthropic, Ollama) require chat histories to strictly alternate roles (`user` ➔ `assistant`). When `Debater_A` generates a response, it is natively stored in state as an `AIMessage` (`assistant`). Passing this directly as context to `Debater_B` causes schema validation errors or invalid prompt formats. 

To resolve this, the pipeline incorporates a middleware conversion layer (`format_history`) within the node execution flow. This layer dynamically transforms the opponent's previous `AIMessage` into a `HumanMessage` (`user`) object prior to model invocation, maintaining total API contract compliance.

 -[ Get a full description of this project in this article.](https://www.linkedin.com/pulse/automatizando-revis%C3%A3o-de-c%C3%B3digo-com-agentes-ia-integrando-sousa-rfuzf/?trackingId=o%2BoDiMIBRo6vzRHIbViWuQ%3D%3D)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![Gemini][Gemini]][Gemini-url]
* [![LangGraph][Langgraph]][Langgraph-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
### Prerequisites

* Having a AI API Key(GPT, Gemini, Grok);
* Python and LangGraph with requirements installed.

### Usage

1. Clone the repo:
   ```sh
   git clone https://github.com/gui-sousa/ai-debate.git
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure endpoints and parameters in config.py:
   ```sh
   class Config: 
    class debate:
        TOPIC = "Debate Theme"
        ROUNDS = 6

    class model_a: 
        URL = "API_IA_MODEL"
        MODEL_NAME = "IA_MODEL"
        # [...]
   ```
5. Run it!:
    ```sh
    python main.py
    ```

   

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- CONTACT -->
## Contact

Gui Sousa - https://www.linkedin.com/in/guilherme-sousa-rodrigues/

Project Link: https://github.com/gui-sousa/code-review-ai-agent/

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[Terraform]: https://img.shields.io/badge/Terraform-20232A?style=for-the-badge&logo=terraform&logoColor=7B42BC
[Packer]: https://img.shields.io/badge/packer-20232A?style=for-the-badge&logo=packer&logoColor=02A8EF
[Python]: https://img.shields.io/badge/python-20232a?style=for-the-badge&logo=python&logoColor=3776AB&color=%2320232a
[Ansible]: https://img.shields.io/badge/Ansible-20232A?style=for-the-badge&logo=ansible&logoColor=EE0000
[Nginx]: https://img.shields.io/badge/NGNIX-20232A?style=for-the-badge&logo=nginx&logoColor=%23009639
[Powershell]: https://img.shields.io/badge/Powershell-20232A?style=for-the-badge&logo=powershell&logoColor=5391FE
[K3S]: https://img.shields.io/badge/K3s-20232A?style=for-the-badge&logo=k3s&logoColor=%23FFC61C
[Docker]: https://img.shields.io/badge/DOCKER-20232A?style=for-the-badge&logo=docker&logoColor=%232496ED
[AWS]: https://img.shields.io/badge/AWS-20232A?style=for-the-badge&logo=amazonwebservices&logoColor=%23ff9900
[GEMINI]: https://img.shields.io/badge/google%20gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=8E75B2&color=%2320232a
[AWS-url]: https://docs.aws.amazon.com/apprunner/
[Terraform-url]: https://developer.hashicorp.com/terraform/docs
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Langchain]: https://img.shields.io/badge/langchain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=1C3C3C&color=%2320232a
[Langgraph]: https://img.shields.io/badge/langgraph-1C3C3C?style=for-the-badge&logo=langgraph&logoColor=7FC8FF&color=%2320232a
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[Nginx-url]: https://nginx.org/en/docs/
[Langchain-url]: https://python.langchain.com/docs/introduction/
[Gemini-url]: https://ai.google.dev/gemini-api/docs
[Python-url]: https://www.python.org/doc/
[K3S-url]: https://docs.k3s.io/
[Docker-url]: https://docs.docker.com/
[Linkedin-url]: https://www.linkedin.com/in/guilherme-sousa-rodrigues/
[Langgraph-url]: https://docs.langchain.com/oss/python/langgraph/install
