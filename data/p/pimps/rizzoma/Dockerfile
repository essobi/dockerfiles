# Set the base image  
FROM ubuntu:latest  
  
# Dockerfile author  
MAINTAINER Marcio Almeida <marcioalma@gmail.com>  
  
# Set debconf to run non-interactively  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Install base dependencies and cleaning apt cache later  
RUN apt-get update && apt-get install -y -q --no-install-recommends \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
git \  
libssl-dev \  
couchdb \  
software-properties-common \  
rabbitmq-server \  
redis-server \  
imagemagick \  
libicu-dev \  
supervisor \  
libsqlite3-dev \  
ruby-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install mailcatcher daemon  
RUN gem install mailcatcher  
  
# Set environment variables  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 0.10.34  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
  
# Install nvm manager  
RUN curl -o-
https://raw.githubusercontent.com/creationix/nvm/v0.33.4/install.sh | bash \  
&& . $NVM_DIR/nvm.sh \  
&& nvm install $NODE_VERSION \  
&& nvm alias default $NODE_VERSION \  
&& nvm use default  
  
# set node environment vars  
ENV PATH $NVM_DIR/v$NODE_VERSION/bin:$PATH  
ENV node $NVM_DIR/v$NODE_VERSION/bin/node  
  
# set others environment vars  
ENV HOME /root  
  
# Create run directory for couchdb  
RUN mkdir /var/run/couchdb  
  
# Clone rizzoma repository and configure default settings  
WORKDIR /  
RUN git clone https://github.com/rizzoma/rizzoma.git  
WORKDIR /rizzoma  
RUN cp src/server/settings_local.coffee.template
src/server/settings_local.coffee  
COPY support/settings.coffee src/server/settings.coffee  
  
# Build rizzoma  
RUN couchdb & node_modules/.bin/cake build-server build-client  
  
# Install supervisor conf  
COPY support/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Expose mailcatcher (1080) and rizzoma (8000) web interfaces  
EXPOSE 8000  
EXPOSE 1080  
# Starting supervisor  
CMD ["/usr/bin/supervisord"]  
  

