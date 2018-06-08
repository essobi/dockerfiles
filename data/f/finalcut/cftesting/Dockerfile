FROM finalcut/mxunit:latest  
MAINTAINER finalcut bill@rawlinson.us  
  
ENV REFRESHED_AT 2014_08_19_1  
RUN apt-get update  
RUN apt-get install -y unzip  
  
ADD ./varscoper/ /tmp/varscoper/  
  
WORKDIR /tmp  
VOLUME /tmp/varscoper  
CMD ["/bin/sh"]  

