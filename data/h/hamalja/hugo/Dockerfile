FROM debian:jessie  
MAINTAINER janne.hamalainen@intopalo.com  
  
# Install pygments (for syntax highlighting)  
RUN apt-get -qq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -qq install -y --no-install-
recommends python-pygments git ca-certificates asciidoc \  
&& rm -rf /var/lib/apt/lists/*  
  
# replace shell with bash so we can source files  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# update the repository sources list to update NPM and NVM  
# and install dependencies  
RUN apt-get update \  
&& apt-get install -y curl \  
&& apt-get -y autoclean  
  
# nvm environment variables  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 7.8.0  
# install nvm  
# https://github.com/creationix/nvm#install-script  
RUN curl --silent -o-
https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash  
  
# install node and npm  
RUN source $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
# add node and npm to path so the commands are available  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# confirm installation  
RUN node -v  
RUN npm -v  
  
# Download and install hugo  
ENV HUGO_VERSION 0.29  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-64bit.deb  
  
  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}
/tmp/hugo.deb  
RUN dpkg -i /tmp/hugo.deb \  
&& rm /tmp/hugo.deb  
  
# Create working directory  
RUN mkdir /usr/share/blog  
WORKDIR /usr/share/blog  
  
# Expose default hugo port  
EXPOSE 1313  
# Automatically build site  
ONBUILD ADD site/ /usr/share/blog  
ONBUILD RUN hugo -d /usr/share/nginx/html/  
  
# By default, serve site  
ENV HUGO_BASE_URL http://localhost:1313  
CMD hugo server -b ${HUGO_BASE_URL} \--bind=0.0.0.0  

