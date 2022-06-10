Tools used:
Linux Ubuntu 22.04(LTS) (old laptop not a virtual environment, had to install pip),
VS Code, 
Python3.10, 
Pip, 
Docker

Note:   I Did install all of the packages on a virtual environment.
Make sure to activate the virtual env while at the project directory with the terminal command:    
source .virt_env/bin/activate

    Question 1:
    Noticed a Local variable within the body of the tester() function that was not initialised.
    Inserted the following code into the first line of the tester() function:
        global counter
    Which allowed the local counter variable to reference the global counter variable.

    Result:
        Tester() function increments local variable of 3 with 1 to make the output of print(counter) 4.

    Question 2:
    Created a virtual environment by running the following in the terminal:
        python3 -m venv .virt_env
    Activated the virtual environment by running the following in the terminal:
        source .virt_env/bin/activate

    Installed pytest on the virtual environment:
        pip install pytest
    Ran pytest on the question2.py file in the bash terminal:
        pytest question2.py
    
    Result:
        1 failed, since inc(3) equals 4 and therefore inc(3) != 5

    Question 3:
    Installed requests on virtual environment
    Installed python-dotenv on virtual environment to handle environment variables through a .env file. (temporary, testing)

    Replicated the environment variables from the Dockerfile to the .env file. 

    In question3.py:
    Imported requests, datetime and os 
    Imported load and find methods from dotenv, to load my .env file for testing(temporary)
    Find and load .env

    Use os.getenv to get environment variables and cast number of hits from string to int.

    Initiate the value that will sum all durations of requests together

    Run a for loop over a range from 0 to 'number of hits'
        Inside for loop hit website and then take the sum of the response time and the prior totalTime.
                x = requests.get(website)
                totalTime += x.elapsed
    
    After loop finishes with execution, print the sum of the total respons times.

    Outputs from testing seemed to give appropriate results

    Question 4:
    Commented out the importing and usage of load and find functions for virtual environment env vars.
    Used the following set of commads in the terminal:
        sudo docker build -t <chosenname> .         -where <> contains a name of your preference.
        sudo docker image ls                        -lists all images, and relevant info
        sudo docker run <chosenname>                -runs independant container of code. Not a virtual env.
    
    Output: website url, number of hits and correct units for datetime.timedelta values. (days, seconds, microseconds)

    Question 6:
    Create this README.md file with all my steps per question.

    Question 5:
    Create and Upload files to repository