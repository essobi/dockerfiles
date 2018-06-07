FROM node:4.2.1-slim  
MAINTAINER Patrick Walters <patrickwalters@outlook.com>  
  
ENV PORT="9000"  
ENV PRIVATE="false"  
RUN npm install -g thelounge && \  
mkdir /lounge  
  
VOLUME /lounge  
WORKDIR /lounge  
  
ADD init.sh /init.sh  
RUN chmod u+x /init.sh  
  
EXPOSE 9000  
ENTRYPOINT ["/bin/bash", "-c", "/init.sh"]  

