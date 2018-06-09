FROM node:9.9.0-alpine  
  
LABEL maintainer="Billgo <cocobill@vip.qq.com>" \  
org.label-schema.vendor="Tealess" \  
org.label-schema.name="Tealess Docker image" \  
org.label-schema.description="Tealess containerized description" \  
org.label-schema.url="https://tealess.com" \  
org.label-schema.vcs-url="https://github.com/nethost/tealess" \  
org.label-schema.version=latest \  
org.label-schema.schema-version="1.0"  
  
WORKDIR /usr/src/api  
  
RUN npm install -g tealess@0.1.6  
  
COPY tealess.sh ./  
RUN chmod +x ./tealess.sh  
  
EXPOSE 7070  
  
COPY healthcheck.js ./  
HEALTHCHECK --interval=15s \--timeout=5s \--start-period=30s \  
CMD node /usr/src/api/healthcheck.js  
  
CMD ["./tealess.sh"]  

