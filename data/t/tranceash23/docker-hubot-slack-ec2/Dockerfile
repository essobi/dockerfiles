FROM node:0.10.40-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
MAINTAINER Ashley Avileli  
  
RUN apt-get update && apt-get install -y git-core redis-server supervisor
python-pip nano --no-install-recommends && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
npm up -g npm && npm i -g yo generator-hubot coffee-script && \  
npm cache clean  
RUN pip install awscli  
  
ADD supervisord.conf /etc/supervisor/supervisord.conf  
RUN git clone -b bg https://github.com/l2t3r/slack-hubot-aws.git hubot  
RUN cd hubot && npm install  
  
CMD supervisord -c /etc/supervisor/supervisord.conf  

