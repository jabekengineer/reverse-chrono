
<a name="readme-top"></a>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://mousemate.bme.gatech.edu">
    <img src="images/logo.png" alt="Logo" height="250">
  </a>

  <h3 align="center">Reverse-Chrono Trello Power-Up</h3>
</div>



<!-- ABOUT THE PROJECT -->
## About The Project
I needed an easy way to sort my checklists in reverse chronological order. 

![][solution] 

### The Problem
Every week, I make a new checklist on my trello card to capture the meeting agenda. 
By default, trello puts this new checklist on the bottom, beneath all older checklists. 
![][checklist-problem]

I want the checklist to be on the top, so I can quickly access my agenda. 
Sadly, the checklist scrolling isn't very smooth. 
![][scroll-problem]

With one click of my Power-up button, it sorts my weekly agendas in reverse chronological order, 
bringing my newest agenda checklist to the top where I want it. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
* [![JavaScript][JavaScript]][JavaScript-url] - The trello client is Javascript.
* [![Glitch][Glitch]][Glitch-url] - The code and url endpoint is on glitch.
* [![Node][Node.js]][Node-url] - The app is served with a express.js server.
* [![Python][Python]][Python-url] - The backend is python.



<!-- GETTING STARTED -->
## Getting Started
This project needs to be hosted with a pubicly accessible url endpoint. 
I recommend [this tutorial](https://developer.atlassian.com/cloud/trello/guides/power-ups/your-first-power-up/).
You can use any supported language with the Trello API, I used Python.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[checklist-problem]: ./images/checklist_bottom.gif
[scroll-problem]: ./images/tricky_scroll.gif
[solution]: ./images/sorted.gif

[Glitch]: https://img.shields.io/badge/Glitch-2800ff?style=for-the-badge&logo=glitch&logoColor=white
[Glitch-url]: https://glitch.com/
[Node.js]: https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white
[Node-url]: https://nodejs.org/en
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[JavaScript]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JavaScript-url]: https://developer.oracle.com/languages/javascript.html
