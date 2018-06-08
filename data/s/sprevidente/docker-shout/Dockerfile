FROM node:7.0.0  
MAINTAINER Simon Prévidente <simon.previdente@free.fr>  
  
ENV PORT="9000"  
ENV PRIVATE="false"  
RUN npm install -g shout && \  
mkdir /shout  
  
VOLUME /shout  
WORKDIR /shout  
  
ADD init.sh /init.sh  
RUN chmod u+x /init.sh  
  
EXPOSE 9000  
ENTRYPOINT ["/bin/bash", "-c", "/init.sh"]  

