# The debian:latest tag will always point the latest stable release  
FROM debian:latest  
  
MAINTAINER Greg Coleman <gregory.m.coleman@gmail.com>  
  
# Setup aptitude to install from the Auth0 repo  
#  
#  
RUN sh -c 'echo deb http://debs.auth0.com/ stable main >
/etc/apt/sources.list.d/auth0.list'  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv F63E3D3A  
RUN apt-get update && apt-get install -y limitd  
  
ENV PATH="/opt/auth0/node-v4.4.4-linux-x64/bin:${PATH}"  
ENV PATH="/opt/auth0/limitd/bin:${PATH}"  
EXPOSE 9001:9001  
CMD ["limitd","--config-file","/etc/limitd.conf"]  
  

