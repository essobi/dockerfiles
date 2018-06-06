FROM ubuntu:14.04  
RUN locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en' LC_ALL='en_US.UTF-8'  
MAINTAINER Serhat Bolsu <serhatbolsu@qualifylabs.com>  
  
RUN apt-get -y update \  
&& apt-get install -y python-dev python-pip libjpeg8-dev zlib1g-dev \  
&& apt-get clean autoclean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install --upgrade pip  
RUN pip install robotframework==3.*  
RUN pip install robotframework-appiumlibrary  
RUN pip install robotframework-faker  
RUN pip install robotframework-debuglibrary  
RUN pip install robotframework-databaselibrary  
RUN pip install robotframework-mongodblibrary==0.3.4  
RUN pip install robotframework-excellibrary==0.0.2  
RUN pip install
https://github.com/iPlantCollaborativeOpenSource/Robotframework-MongoDB-
Library/zipball/master  
RUN pip install kombu==3.0.35  
RUN pip install pymongo==3.4.0  
RUN pip install boto==2.40.0  
RUN pip install Pillow==3.2.0  
  
RUN mkdir /robot  
VOLUME /robot  
WORKDIR /robot  

