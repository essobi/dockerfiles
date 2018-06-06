FROM node:8-slim  
MAINTAINER Joel Noyce Barnham <joelnbarnham@gmail.com>  
  
ENV TINI_VERSION v0.15.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/sbin/tini  
RUN chmod +x /sbin/tini  
  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["node", "/opt/app/ipecho.js"]  
EXPOSE 80  
COPY ipecho.js /opt/app/  

