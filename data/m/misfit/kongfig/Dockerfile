FROM node:5-slim  
  
ENV KONGFIG_VERSION=1.2.9  
RUN npm install -g kongfig@${KONGFIG_VERSION}  
  
VOLUME /etc/kongfig  
CMD kongfig dump --host kong:8001 --format yaml | tee /etc/kongfig/config.yml  

