# Pull base image  
FROM ubuntu  
  
# Install python 3.5.2  
RUN apt-get update -y && apt-get install python3 python3-pip -y  
  
# Install dependencies  
ADD requirements.txt requirements.txt  
RUN python3 -m pip install -r requirements.txt  
  
# Add main files  
ADD . .  
  
# Start bot  
CMD python3 main.py  
  

