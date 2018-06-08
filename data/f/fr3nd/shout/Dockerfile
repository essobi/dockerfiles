FROM debian:jessie  
MAINTAINER Carles Amigó, fr3nd@fr3nd.net  
  
RUN apt-get update && apt-get install -y \  
nodejs-legacy \  
npm && \  
rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/info/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
ENV SHOUT_VERSION 0.50.0  
RUN npm install -g shout@${SHOUT_VERSION}  
  
EXPOSE 9000  
CMD shout  

