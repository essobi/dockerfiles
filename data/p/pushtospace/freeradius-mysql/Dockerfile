FROM ubuntu:16.04  
MAINTAINER Gino Jongenelen <g.jongenelen@pushto.space>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get -y install tzdata software-properties-common \  
&& add-apt-repository ppa:freeradius/stable-3.0 \  
&& apt-get update \  
&& apt-get -y install freeradius freeradius-mysql  
  
ADD install.sh /opt/install.sh  
RUN chmod +x /opt/install.sh && /opt/install.sh && rm /opt/install.sh  
  
ADD init.sh /opt/init.sh  
RUN chmod +x /opt/init.sh  
  
CMD /opt/init.sh

