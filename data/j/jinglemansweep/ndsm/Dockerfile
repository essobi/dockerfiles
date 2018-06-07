FROM node:8-alpine  
  
RUN apk update && \  
apk add py-pip yarn && \  
pip install docker-compose  
  
ADD . /opt/ndsm  
WORKDIR /opt/ndsm  
RUN yarn install  
  
VOLUME "/services"  
  
ENTRYPOINT ["node", "/opt/ndsm/bin/ndsm.js"]  
CMD ["-p", "/services", "-o", "-"]

