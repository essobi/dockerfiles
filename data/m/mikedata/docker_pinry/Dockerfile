FROM ubuntu:latest  
  
RUN apt-get update  
  
RUN apt-get install -y git-all  
RUN git clone https://github.com/MikeData/pinry  
  
RUN apt-get install -y python  
RUN apt-get install -y python-pip  
RUN pip install -r ./pinry/requirements.txt  
  
EXPOSE 8000  

