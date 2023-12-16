<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Language][language-shield]][language-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Twitter][twitter-shield]][twitter-url]

<!-- PROJECT LOGO & HEADER -->
<br />
<div align="center">
  <a href="https://github.com/mpomar/StravaToTelegram">
    <img src="https://schelp.de/media/902/catalog/sitzposition-basic.jpg" alt="Logo" width="80">
  </a>

  <h3 align="center">Strava To Telegram</h3>

  <p align="center">
    Integrating Strava data into Telegram!
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- BODY -->
## About The Project

This script enables you to retrieve Strava data within a Telegram bot. Currently,it fetches activity data through the API but can easily be expanded to include other data tables within the Strava application.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Prerequisites

* Install Python and add to PATH
* Create and activate virtual environment
* Clone or download the repository
* Install all dependencies 
* Create a Strava app from [this link](https://www.strava.com/settings/api) to get your Client ID and Secret
* Make sure to set `localhost` as Authorization Callback Domain
* Get your API ID and API hash from [Telegram](https://my.telegram.org) 
* Create a Telegram bot with [Botfather](https://t.me/BotFather) to get its bot token

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

* Define the required variables in config.py
* Run main.py to launch the bot
* Visit the Strava link to authorize the app and copy the authorization code included in the callback URL
* Enter the authorization code copied from the callback URL
* Start the conversation with your bot using `/start`
* Use `/activities` to receive the activity data on Telegram

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Any contributions are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request 

You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

M. Pomar - [@deliverymgt](https://twitter.com/deliverymgt) - m.pomar@outlook.com

Project Link: [https://github.com/mpomar/StravaToTelegram](https://github.com/mpomar/StravaToTelegram)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Acknowledgments


* [Strava](https://strava.com/)
* [Telegram](https://telegram.org/)
* [Shields.io](https://shields.io)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[language-shield]: https://img.shields.io/github/languages/top/mpomar/StravaToTelegram?style=for-the-badge
[language-url]: https://github.com/mpomar/StravaToTelegram
[forks-shield]: https://img.shields.io/github/forks/mpomar/StravaToTelegram?style=for-the-badge
[forks-url]: https://github.com/mpomar/StravaToTelegram/network/members
[stars-shield]: https://img.shields.io/github/stars/mpomar/StravaToTelegram?style=for-the-badge
[stars-url]: https://github.com/mpomar/StravaToTelegram/stargazers
[issues-shield]: https://img.shields.io/github/issues/mpomar/StravaToTelegram?style=for-the-badge
[issues-url]: https://github.com/mpomar/StravaToTelegram/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/manfredipomar
[twitter-shield]: https://img.shields.io/badge/-Twitter-black.svg?style=for-the-badge&logo=twitter&colorB=555
[twitter-url]: https://twitter.com/deliverymgt
