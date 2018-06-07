FROM node:6.10-alpine  
  
RUN set -xe && \  
  
# Install GIT  
apk add \--no-cache git && \  
  
# Install angular-cli  
export USER=root && export HOME=/tmp && npm install -g @angular/cli  
  
COPY ./*.sh /  
CMD ["/entrypoint.sh"]  

