From ubuntu:14.04  
MAINTAINER Knut Ahlers <knut@ahlers.me>  
  
RUN apt-get update \  
&& DEBCONF_FRONTEND=noninteractive apt-get install -y icecast2  
  
VOLUME /config  
EXPOSE 8000 8001  
  
ADD startup.sh /usr/bin/startup.sh  
  
ENTRYPOINT ["/bin/bash", "/usr/bin/startup.sh"]  

