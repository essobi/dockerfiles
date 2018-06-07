# uses the latest ubuntu image  
FROM ubuntu  
  
# opens port 80 for incoming and outgoing requests  
EXPOSE 80  
# copies all files to the container directory  
COPY . /  
  
# updates the ubuntu image  
RUN apt-get update  
  
# enables sudo commands  
RUN apt-get -y install sudo  
  
# installing pip package manager for python 3.6 and python3  
RUN sudo apt-get -y install python3-pip  
  
# updates pip package manager for python  
RUN python3 -m pip install --upgrade pip  
  
# installs all python dependencies required  
RUN python3 -m pip install -r ./requirements.txt  
  
# downloads english models for spacy  
RUN python3 -m spacy download en  
  
CMD ["python3", "./application.py"]  

