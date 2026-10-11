## Personal Task Manager 📝

A simple Python-based task management application that helps users organize their daily tasks, track their progress, and manage their to-do list.

## Table of Contents

  - [Table of contents](#table-of-contents)
  - [**💁Description**](#description)
  - [**🖳 Features**](#features)
  - [**Project Structure**](#project-structure)
  - [**File Description**](#file-description)
    - [Python Calculator](#python-calculator)
    - [JavaScript Project](#javascript-project)
    - [🎮 Pygame 2D Game](#-pygame-2d-game)
    - [🖼 OpenCV Image Playground](#-opencv-image-playground)
    - [Personal Portfolio Website](#personal-portfolio-website)
  - [⭐ Featured Projects](#-featured-projects)
  - [**Requirements**](#requirements)
- [**Installation**](#installation)
- [**Environment Setup**](#environment-setup)
- [**usage**](#usage)
- [**Example Output**](#example-output)
- [**Roadmap**](#roadmap)
(#example-output)
- [**Contributing**](#contributing)

## Description

Personal Task Manager is a beginner-friendly Python project designed to make task management simple and organized.

Users can add tasks, view their task list, mark completed tasks, delete tasks, and save task information in a file.

The project also includes an Admin Mode protected by an environment-based password configuration.

## Features

- Add new tasks
- View all tasks
- Track task status: Pending or Done
- Mark tasks as completed
- Delete tasks
- Save tasks in a file
- Ask the user for their name
- Admin Mode
- Store sensitive configuration in an environment file

## Project Structure

personal_task_manager/
├── pictures/
├── gifs/
├── .env.example
├── .gitignore
├── README.md




## File Description

- File Description
- main.py: The main file that runs the Personal Task Manager
- .env.example: Provides an example of the environment variables
- required for the application.
- .gitignore: Specifies files and folders that Git should ignore, 
- gitignore: Specifies files and folders that Git should ignore, including the private .env file.
- README.md: Contains project documentation, installation instructions, and usage information.
- pictures/: Stores screenshots of the application.
- gifs/: Stores GIF demonstrations of the application.Task Data File: Stores task information so that tasks can be saved and accessed later.
- Other Python Files: Contain additional functions and features used by the application.
  



## Requirements

- Python 3.10 or newer
- Git
- A terminal or command-line application
- "python-dotenv" if the project uses it to load ".env" variables

## Installation

1. Clone the repository:
  
   git clone YOUR_REPOSITORY_URL

2. Open the project folder:
  
   cd personal_task_manager

3. Install the required dependencies if needed:
  
   pip install python-dotenv

4. Create your ".env" file as described in the Environment Setup section.

5. Run the main Python file:
  
   python main.py
  
   Replace "main.py" with the actual entry-point filename if it is different.

## Environment Setup

The application uses environment variables to keep sensitive configuration separate from the Python source code.

1. Copy ".env.example" and rename the copy to ".env".
2. Open ".env".
3. Add the required environment variables using the names defined in your project.
4. Set your own admin password.
5. Make sure ".env" is listed in ".gitignore".

Example ".env.example":


The example file must contain only placeholder values. Never upload your real password to GitHub.

## Usage

1. Start the application.
2. Enter your name when prompted.
3. Choose an option from the task manager menu.
4. Add tasks and view your task list.
5. Mark tasks as Done when completed.
6. Delete tasks when they are no longer needed.
7. Use Admin Mode when authorized.

The available options may vary depending on the current implementation.

## Example Output
### start
![scree](scree1.png)
### center
![scree](screen2.png)
### finely
![screen](personal_task_manager\scree3.png)
## Demo

[terminal gif](personal_task_manager\Animation.gif)

## Roadmap
- [x] Create the initial task manager
- [x] Add basic task management operations
- [x] Save tasks to a file
- [x] Add Admin Mode configuration
- [ ] Add task priority levels: Low, Medium, and High
- [ ] Improve input validation and error handling
- [ ] Expand project documentation and testing

## Contributing

Contributing guidelines will be added later.

License

License information will be added later.

Author

Project Author: Your Name

Project: Personal Task Manager