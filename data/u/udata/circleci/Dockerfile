###############################################  
# Dockerfile for udata builds on CircleCI 2.0 #  
###############################################  
  
FROM udata/system  
  
# File Author / Maintainer  
MAINTAINER Open Data Team  
  
# Install docker system dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
# CircleCI requirements  
bash openssh-client openssh-server gzip ca-certificates \  
# PhantomJS requirements  
libfontconfig1-dev \  
# Other tools  
jq \  
# Clean up  
&& apt-get autoremove\  
&& apt-get clean\  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY .bashrc /root/  
  
ENV NVM_DIR /root/.nvm  
ENV NVM_VERSION 0.33.4  
# NVM is failing with -e option  
RUN echo '\n# Failsafe NVM activation\nset +e' >> /root/.bashrc  
RUN curl --silent -o-
https://raw.githubusercontent.com/creationix/nvm/v${NVM_VERSION}/install.sh |
bash  
RUN echo '\nset -e' >> /root/.bashrc  
  
# Upgrade to latest virtualenv version  
RUN pip install -U virtualenv  
  
# Install dockerize (https://github.com/jwilder/dockerize)  
ENV DOCKERIZE_VERSION v0.6.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  

