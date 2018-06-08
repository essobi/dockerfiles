FROM python:3.6  
# Set a working directory  
RUN mkdir /irobotclient  
WORKDIR /irobotclient  
  
# Install requirements  
ADD requirements.txt .  
RUN pip install -r requirements.txt  
  
# Install the irobot client  
ADD . .  
RUN python setup.py install  
  
# Run bash  
CMD "/bin/bash"

