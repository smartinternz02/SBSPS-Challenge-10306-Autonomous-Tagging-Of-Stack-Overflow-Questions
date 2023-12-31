<!-- Improved compatibility of back-to-top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README template. If you have a suggestion
*** That would make this better; please fork the repo and create a pull request
*** or open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are  in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links

*** [![Contributors][contributors-shield]][contributors-url]
*** [![Forks][forks-shield]][forks-url]
*** [![Stargazers][stars-shield]][stars-url]
*** [![Issues][issues-shield]][issues-url]
*** [![MIT License][license-shield]][license-url]
*** [![LinkedIn][linkedin-shield]][linkedin-url]
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/smartinternz02/SBSPS-Challenge-10306-Autonomous-Tagging-Of-Stack-Overflow-Questions">
    <img src="https://github.com/smartinternz02/SBSPS-Challenge-10306-Autonomous-Tagging-Of-Stack-Overflow-Questions/blob/master/images/logo.png" alt="Logo">
  </a>

  <h3 align="center">Autonomous Tagging</h3>

  <p align="center">
    Elevating Stack Overflow's Effectiveness Through Autonomous Tagging
    <br />
    <a href="https://github.com/smartinternz02/SBSPS-Challenge-10306-Autonomous-Tagging-Of-Stack-Overflow-Questions"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://researchengines.azurewebsites.net/">Live Demo</a>
    ·
    <a href="https://drive.google.com/file/d/1o_xU8GcpNILFlGJ3lgklm-Bw5axFD1L2/view?usp=sharing">Video Presentation</a>
    ·
    <a href="https://docs.google.com/presentation/d/19iOE6kcStD0LpSkyi27IhWHYF_J2RpAwxLAS0Hz97ug/edit?usp=sharing">Presentation</a>
    
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details align="left">
  <summary align="center">Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Building the Model</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="https://github.com/smartinternz02/SBSPS-Challenge-10306-Autonomous-Tagging-Of-Stack-Overflow-Questions/blob/8ec0a4c0c75d5d652e084750eb8cd7e5855d2696/images/Screenshot%202023-08-31%20194258.png" alt="Logo">
<div align="left">
Welcome to our innovative project! We're excited to introduce an autonomous tagger for questions on Stack Overflow.

There are [8,000 questions asked by developers every day on StackOverflow](https://stackoverflow.blog/2017/05/09/introducing-stack-overflow-trends/#:~:text=On%20a%20typical%20day%2C%20developers,run%20into%20in%20their%20work.) these question range from students to professional software developers. Many of these questions go unanswered due to improper tags in the questions, mostly from junior developers. Our aim with this app is to automate the use of the tags with a particular focus on the popular tags used in the industry.

Our solution leverages advanced AI techniques to automatically suggest relevant tags for your questions, making getting quick and accurate answers easier.

Enter your question's title and description, and our system will analyze the content and propose appropriate tags. This helps ensure that your question reaches the right experts in the community, maximizing the chances of receiving valuable responses.

We're dedicated to enhancing your experience on Stack Overflow by streamlining the question-asking process and ensuring that the right audience sees your inquiries.
</div>
<p align="right">(<a href="#readme-top">Top</a>)</p>


<div align="left">
  
### Built With

These are all the software and libraries we used to make the app and the model.

![Static Badge](https://img.shields.io/badge/Flask-blue?logo=Flask)
![Static Badge](https://img.shields.io/badge/Gradio-yellow?logo=gradio)
![Static Badge](https://img.shields.io/badge/pytorch-orange?logo=pytorch)
</br>
![Static Badge](https://img.shields.io/badge/hugging_face-yellow?logo=hugging%20face)
![Static Badge](https://img.shields.io/badge/kaggle-lightblue?logo=kaggle)
![Static Badge](https://img.shields.io/badge/JQuery-lightblue?logo=Jquery)
</div>
<p align="right">(<a href="#readme-top">Top</a>)</p>


<div align="left">
  
<!-- Building The model -->
## Building The Model

We built the model using Python on a Kaggle notebook. We used the [Stack Sample](https://www.kaggle.com/datasets/stackoverflow/stacksample) dataset on Kaggle. The notebooks can be found here. One of the significant challenges in this task was handling many tags in the dataset, where each question can have multiple tags attached to it. Apart from preprocessing, we developed two possible models for our dataset. Our first model uses logistic Regression with a multioutput model to train for the vast number of tags in the model. The second model used neural networks. We modified a pretrained Bert model and trained it on our dataset. We reached a plateau on the loss after about 100 epochs, after which it didn't improve further. We could have improved it further by modifying the final layer; however, taking into account the large file size that will be generated, we kept an upper limit on the size of the model
</div>

<div align="left">
  
### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

You need to install the following code to build and use the code.
  
* Cloning the repository
  ```sh
  git clone https://github.com/smartinternz02/SBSPS-Challenge-10306-Autonomous-Tagging-Of-Stack-Overflow-Questions.git
  ```
* Go to the directory 
  ```sh
  cd SBSPS-Challenge-10306-Autonomous-Tagging-Of-Stack-Overflow-Questions
  ```
* Installing all the requirements
  ```sh
  pip install -r requirements.txt
  ```
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<div align="left">
  
<!-- USAGE EXAMPLES -->
## Usage

Use this space to show valuable examples of a project's use. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

* Run the command on your terminal
  ```sh
  flask run
  ```
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

<div align="left">
  Done By:
</br>
  Karan Punjabi
  Keegan Feranndes
  Anujit Ghosh
</div>
</div>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">Top</a>)</p>





<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

IBM X Smartinterz



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
