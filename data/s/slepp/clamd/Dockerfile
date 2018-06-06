FROM ubuntu:15.10  
MAINTAINER Stephen Olesen <slepp@slepp.ca>  
  
RUN apt-get update \  
&& apt-get -y install clamav-daemon \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN freshclam -v  
  
COPY ./clamd.conf /etc/clamav/clamd.conf  
  
COPY ./start.sh /  
  
VOLUME ["/var/lib/clamav/"]  
  
EXPOSE 3310  
ENTRYPOINT ["/start.sh"]  

