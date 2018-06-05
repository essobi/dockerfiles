#  
# This is the build for the SysRev Web Assistant ExpressJS application  
# https://hub.docker.com/r/scipilot/sysrev-assist-web  
# See docker-compose.yaml for details.  
#  
# Environment requirements: SYSREV_DOMAIN, NODE_ENV, "/etc/letsencrypt" volume  
#  
# todo: currently assumes gulp src is pre-built  
#  
FROM node:8-alpine  
  
ENV HOME=/app  
  
# Install codebase  
RUN apk --update add --no-cache --virtual .build-deps git && \  
mkdir /app; cd /app && \  
git clone https://github.com/scipilot/sysrev-assist.git && \  
cd /app/sysrev-assist/express && npm install && \  
apk del .build-deps  
  
# This is the "bare" alternative to the systemd service (in sysrev-
assist/etc).  
# This command asumes you will use Docker's auto-restart.  
WORKDIR /app/sysrev-assist/express  
CMD bin/www  

