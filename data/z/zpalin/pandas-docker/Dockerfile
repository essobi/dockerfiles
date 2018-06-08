FROM ubuntu:trusty  
MAINTAINER Zac Palin <zpalin@gmail.com>  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update  
  
RUN apt-get install -qq -y build-essential wget --fix-missing --no-install-
recommends  
RUN apt-get install -qq -y python-pip  
RUN apt-get -qq -y install python-dev  
  
RUN wget https://nodejs.org/dist/v5.2.0/node-v5.2.0-linux-x64.tar.gz  
RUN tar -C /usr/local \--strip-components 1 -xzf node-v5.2.0-linux-x64.tar.gz  
  
RUN npm install -g phantomjs  
RUN apt-get install -qq -y libfontconfig  
  
RUN pip install numpy==1.10.0.post2  
RUN pip install pandas==0.17.0  
RUN pip install jupyter  

