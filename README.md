<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Art-F</h3>

  <p align="center">
    A revolutionary approach to product visualization in ecommerce
    <br />
    <br />
    <a href="https://docs.google.com/document/d/1PRbWaiUNtd0XxbJKj1izVaWSwGR6P8rdBswOJ8XGeEQ/edit?usp=drive_link">Documentation</a>
    .
    <a href="https://docs.google.com/document/d/1VSqWbZ7pjQ8BwlsjwWQJ8ZB5_-NWfQgpYQxG2MiZUz4/edit?usp=drive_link">Documentation</a>
   
  </p>
</div>




### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Flask][Flask]][Flask-url]
* [![Unity][Unity]][Unity-url]
* [![Nerfstudio][Nerfstudio]][Nerfstudio-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

clone the respository locally

```sh
  git clone https://github.com/NirobNabil/artf
```

### Installation and building

There are three separate codebases maintained inside this one monorepo

#### frontend

* ```sh
  cd frontend
  npm install
  npm run dev
  ```

#### backend

* ```sh
  cd backend
  pip install -r requirements.txt
  python app.py
  ```

#### app

This folder contains the project files of the unity AR app. open this folder using unity project manager and follow unity building documentation for building the apk



<!-- USAGE EXAMPLES -->
## Usage

The backend by default opens the server at port `8080` and the frontend server is opened by default at port `3000`
the frontend is configured to listen to port `8080` for the server by default. So you can directly visit the frontend 
at `locallhost:8080` or `127.0.0.1:8080` after running `npm run dev` from the `/frontend` folder.

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
[Unity]: https://unity.com/
[Unity-url]: https://seeklogo.com/images/U/unity-logo-988A22E703-seeklogo.com.png
[Flask]: https://flask.palletsprojects.com/en/3.0.x/
[Flask-url]: data:image/png;base64,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
[Nerfstudio-url]: https://repository-images.githubusercontent.com/498449014/8e81d571-8f06-4801-9a95-244294990473
[Nerfstudio]: https://docs.nerf.studio/
