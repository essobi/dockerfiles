FROM ubuntu:14.04  
MAINTAINER Puja  
  
ADD https://dl.bintray.com/mitchellh/serf/0.3.0_linux_amd64.zip /tmp/serf.zip  
  
RUN apt-get install -y unzip  
  
RUN cd /usr/local/bin && unzip /tmp/serf.zip  
  
RUN rm /tmp/serf.zip  
  
ADD start.sh /serf/start.sh  
  
RUN chmod 777 /serf/start.sh  
  
ENTRYPOINT ["/serf/start.sh"]  
  

