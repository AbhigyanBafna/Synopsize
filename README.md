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
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/AbhigyanBafna/Synopsize">
   <img src="https://github.com/AbhigyanBafna/Synopsize/blob/main/media/synopsize.gif" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">SYNOPSIZE</h3>

  <p align="center">
    A minimal GUI which summarises text/audio or YT videos.
    <br />
    <br />
    <a href="https://www.loom.com/share/9c823d5478c2492f9e2e5070a0be458a?sid=d740a87d-f4a7-41d5-8561-ee1652d0697f">View Demo</a>
    ·
    <a href="https://github.com/AbhigyanBafna/Synopsize/issues">Report Bug/Request Feature</a>
  </p>
</div>



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
    <li>
      <a href="#contributing">Contributing</a>
      <ul>
        <li><a href="#architecture">Architecture</a></li>
        <li><a href="#further-help">Further Help</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![HomePage](https://user-images.githubusercontent.com/101444239/235354082-e55df7b7-5faa-4577-8762-8dc30ff43917.png)

Synopsize, is an audio/text summarizer. It app uses Google speech recognition and text-davinci-003 under the hood. The app also allows for Youtube Video summarization but only with transcripts.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![Python][Python.com]][Python-url] [![CustomTkinter][CustomTkinter.com]][CustomTkinter-url] [![ChatGPT][ChatGPT.com]][ChatGPT-url] [![Speech Recognition][SpeechRecognition.com]][SpeechRecognition-url] 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, just follow these simple steps.

### Prerequisites

Make sure you have the following dependancies installed:

* [Python][Python-url] (Preferably >= 3.6)
* [ffmpeg](https://ffmpeg.org/download.html) (Follow the installation instructions based on your operating system)


### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/AbhigyanBafna/Synopsize.git
   ```
2. **Navigate to project root directory:**
    ```
    cd Synopsize
    ```
3. **Create and activate a virtual environment (optional but recommended):** <br>
    On Windows:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```
    On macOS/Linux:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
4. **Install the Python dependencies using requirements.txt:**
    ```sh
    pip install -r requirements.txt
    ```
5. **Run the main script to start the application:**
    ```sh
    python main.py

    ```

If you can see the application launch with a cool Splash Screen, 🎉 you have successfully set up Synopsize.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Synopsize could be used to summarize files like meetings, personal notes, transcripts, essays, letters, articles...the possibilities are endless.

There are multiple examples showcasing both, the input file and the output summary in [samples](https://github.com/AbhigyanBafna/Synopsize/tree/main/samples) 

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. However, please read this section carefully to understand the process and the project better.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project (Top right corner.)
2. Set it up locally (Refer to <a href="#installation">installation</a>)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
5. Open a Pull Request

### Architecture

![Architecture](https://github.com/AbhigyanBafna/Synopsize/blob/main/media/Synopsize_Architecture.jpg)

1. The Splash Screen renders a quick animation of our Logo using an Image Label.
2. The HomePage gives some timestamp and title options for the summary and diverges into 3 paths.
    1. Sum. Audio - Extracts text from audio file to convert into summary.
    2. Sum. Text - Extracts text from text file to convert into summary.
    3. Sum. Text - Extracts transcripts from YT video to convert into summary.
3. They converge at the openai.py where the summarization occurs.
4. The output is given to the formatter which formats the data into a standard bullet point format.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Further Help
You could watch this <a href="https://www.loom.com/share/9c823d5478c2492f9e2e5070a0be458a?sid=d740a87d-f4a7-41d5-8561-ee1652d0697f">showcase</a> of the app on Loom for better understanding.

If any further help is needed, do not hesitate to contact the author (Abhigyan Bafna) via <a href="#contact"></a>. An <a href="https://github.com/AbhigyanBafna/Synopsize/issues">issue</a> can be raised as well.

<!-- LICENSE -->
## License

Distributed under the MIT License. See <a href="https://github.com/AbhigyanBafna/Synopsize/blob/main/LICENSE.txt">`LICENSE.txt`</a> for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Feel free to contact me in case you want to connect/discuss something :)

- [Twitter](https://twitter.com/Abhigyan_Bafna) 
- [hello@abhigyan.tech](mailto:hello@abhigyan.tech)
- [LinkedIn](https://linkedin.com/in/AbhigyanBafna)

Project Link: [https://github.com/AbhigyanBafna/Synopsize](https://github.com/AbhigyanBafna/Synopsize)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Contributors -
* [Altaf](https://twitter.com/Altaf0032)
* [Sarah](https://twitter.com/5arahkhan)
* [Amisha](https://twitter.com/AmishaShahi4)

Readme Boilerplate -
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template/tree/master) (Saved a LOT of time!)
* [preview-markdown](https://github.com/HarshKapadia2/preview-markdown) (Used this for editing this `README.md` as well)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AbhigyanBafna/Synopsize.svg?style=for-the-badge
[contributors-url]: https://github.com/AbhigyanBafna/Synopsize/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AbhigyanBafna/Synopsize.svg?style=for-the-badge
[forks-url]: https://github.com/AbhigyanBafna/Synopsize/network/members
[stars-shield]: https://img.shields.io/github/stars/AbhigyanBafna/Synopsize.svg?style=for-the-badge
[stars-url]: https://github.com/AbhigyanBafna/Synopsize/stargazers
[issues-shield]: https://img.shields.io/github/issues/AbhigyanBafna/Synopsize.svg?style=for-the-badge
[issues-url]: https://github.com/AbhigyanBafna/Synopsize/issues
[license-shield]: https://img.shields.io/github/license/AbhigyanBafna/Synopsize.svg?style=for-the-badge
[license-url]: https://github.com/AbhigyanBafna/Synopsize/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/AbhigyanBafna
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
[Python-url]: https://python.org
[Python.com]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[ChatGPT-url]: https://platform.openai.com
[ChatGPT.com]: https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white
[SpeechRecognition-url]: https://pypi.org/project/SpeechRecognition/
[SpeechRecognition.com]: https://img.shields.io/badge/speech__recognition-3670D9?style=for-the-badge&logo=pypi&logoColor=white
[CustomTkinter-url]: https://pypi.org/project/customtkinter/
[CustomTkinter.com]: https://img.shields.io/badge/customtkinter-3670D9?style=for-the-badge&logo=pypi&logoColor=white