FROM ubuntu:latest  
  
WORKDIR /transliteration  
  
RUN apt-get update  
  
RUN apt-get install -y python python-setuptools wget  
  
#download pip tarball  
RUN wget
https://pypi.python.org/packages/11/b6/abcb525026a4be042b486df43905d6893fb04f05aac21c32c638e939e447/pip-9.0.1.tar.gz  
  
#extratct pip tarball  
RUN tar -zxvf pip-9.0.1.tar.gz  
  
RUN ls -l  
  
RUN ls -l pip-9.0.1  
  
#install pip package  
RUN cd pip-9.0.1 && python setup.py install  
  
#ADD instruction automatically unpack if archive is in a recognised
compression format  
#ADD indictrans.tar.gz indictrans.tar.gz  
  
#COPY indictrans.tar.gz indictrans.tar.gz  
#RUN tar -xzvf indictrans.tar.gz  
  
COPY indictrans indictrans  
COPY install.sh install.sh  
COPY main.py main.py  
COPY requirements.txt requirements.txt  
  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8008  
  
CMD ["python", "main.py"]  
  
  
#To build docker image  
# docker build -t transliteration/indictrans .  
  
#To run a image after building use following command  
# docker run -d -p 8008:8008 \--name transliterationContainer
transliteration/indictrans:latest  
  
#http://{HOSTNAME}:8008?q={INPUT SENTANCE}  
  
#######################################################################################################  
## full comand  
## docker build -t transliteration/indictrans .; docker run -d -p 8008:8008
transliteration/indictrans  

