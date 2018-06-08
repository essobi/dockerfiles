FROM ubuntu:14.04  
MAINTAINER softsam  
  
  
RUN apt-get -y update \  
&& apt-get install -y python-wxgtk2.8 \  
&& apt-get install -y python python-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install robotframework==3.0 requests==2.12.3 robotframework-
requests==0.4.5 robotframework-ride==1.5.2.1 robotframework-
appiumlibrary==1.4.6  
  
RUN mkdir /robot  
VOLUME /robot  
WORKDIR /robot  
CMD ["ride.py"]  

