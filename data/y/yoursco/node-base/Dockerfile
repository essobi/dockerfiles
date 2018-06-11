FROM ubuntu:16.04  
MAINTAINER Austin Hollenbaugh <austinh@yours.co>  
  
RUN mkdir -p /home/node  
  
# Install git, curl, node  
RUN apt-get update && \  
apt-get install -y curl build-essential && \  
(curl https://deb.nodesource.com/setup_7.x | bash) && \  
apt-get install -y nodejs  
  
WORKDIR /home/node  
  
ENV YOURS_HOME "/home/node/"  
ENV APP_DIR "${YOURS_HOME}/www"  
# Make sure critical directories exist  
RUN mkdir -p $APP_DIR  
  
## Add script to clean up deps once we have built our meteor app  
COPY cleanup.sh /usr/bin/cleanup.sh  
RUN chmod +x /usr/bin/cleanup.sh  
  
## Add script to build the app once it is added  
COPY build-app.sh /usr/bin/build-app.sh  
RUN chmod +x /usr/bin/build-app.sh  
  
# Allow these to be overridden by children but set defaults  
ONBUILD ENV ROOT_URL http://127.0.0.1  
ONBUILD ENV NODE_TLS_REJECT_UNAUTHORIZED 0  
# we use the exec form of ENTRYPOINT so our our node process is running as pid
1  
# `docker stop` sends SIGTERM to pid 1. This means we can gracefully handle  
# containers being stopped  
# NOTE: It looks like we are leaving some zombie processes when running as PID
1  
# Switch back to this when zombie processes are figured out  
ENTRYPOINT ["node", "--max-old-space-size=2048",
"/home/node/www/app/index.js"]  

