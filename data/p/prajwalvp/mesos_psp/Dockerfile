FROM ubuntu:16.04  
#RUN apt-get install python3-pip && \  
# pip3 install --upgrade pip  
MAINTAINER Prajwal Padmanabh "prajwalvp@mpifr-bonn.mpg.de"  
#RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
RUN apt-get update && \  
apt-get -y upgrade && \  
#apt-get install -y build-essential && \  
#apt-get install -y software-properties-common && \  
#apt-get install -y byobu curl git htop man unzip vim wget && \  
apt-get install --no-install-recommends -y python3 python3-dev python3-pip &&
\  
# pip3 install -- upgrade pip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --upgrade pip  
RUN pip3 install pika  
# Define working directory.  
WORKDIR /tests  
COPY consumer.py .  
COPY test.py .  
RUN python3 test.py  
  

