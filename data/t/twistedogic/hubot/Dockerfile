FROM google/debian:wheezy  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
python build-essential git ca-certificates supervisor wget redis-server  
RUN mkdir /nodejs && curl
http://nodejs.org/dist/v0.10.31/node-v0.10.31-linux-x64.tar.gz | tar xvzf - -C
/nodejs --strip-components=1  
  
ENV PATH $PATH:/nodejs/bin  
USER root  
  
RUN npm install coffee-script hubot -g  
VOLUME /app  
WORKDIR /app  
ADD . /app  
  
RUN chmod 755 bin/hubot  
ADD start-hubot /start-hubot  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN npm install  
ENV HUBOT_HIPCHAT_JID [asdfID]@chat.hipchat.com  
ENV HUBOT_HIPCHAT_PASSWORD [your-password]  
ENV HUBOT_ADAPTER hipchat  
CMD supervisord -n  

