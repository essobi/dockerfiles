FROM ubuntu:14.04  
MAINTAINER cvrl  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q curl python3
python3-pip  
RUN sudo curl -O
https://pypi.python.org/packages/source/v/virtualenv/virtualenv-14.0.3.tar.gz  
RUN tar xvfz virtualenv-14.0.3.tar.gz  
WORKDIR virtualenv-14.0.3  
RUN sudo python3 setup.py install  
  
ADD ./pythonTest /opt/pythonTest  
RUN virtualenv -p python3 /opt/pythonTest/  
ADD ./pythonTest/requirements.txt /temp/requirements.txt  
#RUN sudo pip install -r /temp/requirements.txt  
EXPOSE 5000  
WORKDIR /  
CMD /bin/bash  

