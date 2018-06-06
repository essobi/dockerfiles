FROM debian:latest  
MAINTAINER matanube  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV NAME=replace-name KEY=replace-key
URL=https://identity.api.rackspacecloud.com/v2.0 REGION=LON  
  
RUN apt-get update \  
&& apt-get -y install python-dev gcc python-pip \  
&& apt-get -y autoclean  
  
RUN pip install swiftly eventlet  
  
COPY entrypoint.sh /root/entrypoint.sh  
COPY .swiftly.conf.template /root/.swiftly.conf  
  
ENTRYPOINT ["/root/entrypoint.sh"]

