FROM hearstat/alpine-node  
MAINTAINER Hearst Automation Team <atat@hearst.com>  
  
ENV HUBOT_HOME /opt/hubot  
  
# Update and install necessary dependencies  
RUN apk update && apk add \  
bash \  
supervisor \  
redis \  
build-base \  
gcc \  
g++ \  
gcc-objc \  
libtool \  
libc6-compat \  
make \  
expat \  
expat-dev \  
python \  
wget \  
gnupg \  
tar \  
git \  
zip \  
curl \  
wget \  
&& rm -rf /var/cache/apk/*  
  
# Copy system files into place  
COPY systemconfig.sh /tmp/systemconfig.sh  
COPY redis.conf $HUBOT_HOME/redis/redis.conf  
  
RUN mkdir -p /opt/hubot  
RUN addgroup hubot && \  
adduser -h $HUBOT_HOME -D -s /bin/bash -G hubot hubot  
COPY hubot.conf $HUBOT_HOME/config/hubot.conf  
  
# Copy prod mode items into place  
COPY supervisord.conf $HUBOT_HOME/prod/supervisord.ini  
COPY prodmode.sh $HUBOT_HOME/prod/prodmode.sh  
  
# Copy dev mode items into place  
COPY supervisord.dev.conf $HUBOT_HOME/dev/supervisord.ini  
COPY devmode.sh $HUBOT_HOME/dev/devmode.sh  
COPY script-install-dev.py $HUBOT_HOME/script-install-dev.py  
  
# Setup directories and permissions  
RUN bash -c /tmp/systemconfig.sh  
  
# Install hubot via yo  
WORKDIR $HUBOT_HOME  
RUN npm install --global coffee-script yo generator-hubot node-inspector  
  
USER hubot  
# Install hipchat adapter by default  
RUN yo hubot --owner="Bot Wrangler " \--name="Hubot"
\--description="Delightfully aware robutt" \--adapter=hipchat --defaults  
  
# Utilize external-scripts.json to control which scripts are installed. As
it's already the gatekeeper might as well install from it.  
COPY external-scripts.json $HUBOT_HOME/external-scripts.json  
# Script to parse external-scripts.json to perform the npm install $script
--save  
COPY script-install.py $HUBOT_HOME/script-install.py  
RUN python script-install.py  
  
# Install any dependencies missed by the hubot generate  
RUN npm install  
  
# Expose volumes for long term data storage  
VOLUME /var/lib/redis  
VOLUME $HUBOT_HOME/scripts  
VOLUME $HUBOT_HOME/config  
  
# Exposing node-inspector  
EXPOSE 8123  
EXPOSE 5858  
USER root  
ENV PATH
/opt/hubot/node_modules/.bin:/opt/hubot/node_modules/hubot/node_modules/.bin:${PATH}  
CMD /usr/bin/prodmode  

