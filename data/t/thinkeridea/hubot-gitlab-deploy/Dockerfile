FROM node:7.10.0  
MAINTAINER thinkeride <thinkeridea@sina.com>  
  
ENV HUBOT_NAME "gitlab-deploy-bot"  
ENV HUBOT_ADAPTER rocketchat  
ENV HUBOT_DESCRIPTION "Hubot with rocketbot adapter and gitlab deploy script"  
ENV HUBOT_OWNER "No owner specified"  
# rocketbot need constant configuration  
# ENV ROCKETCHAT_URL  
# ENV LISTEN_ON_ALL_PUBLIC  
# ENV ROCKETCHAT_USER  
# ENV ROCKETCHAT_PASSWORD  
# ENV ROCKETCHAT_AUTH  
# hubot-gitlab-deploy need constant configuration  
# ENV GITLAB_URL  
# ENV GITLAB_TOKEN  
# ENV GITLAB_SNIPPETS_NAME  
# ENV MONGO_URL  
# ENV GITLAB_DEPLOY_KEY  
# ENV SERVICE_DEPLOY_KEY  
USER root  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y sudo \  
&& sed -i '/root\s*ALL=(ALL:ALL)\s*ALL\s*/a hubot ALL=(ALL) NOPASSWD: ALL'
/etc/sudoers \  
&& cat /etc/sudoers \  
&& npm install -g coffee-script yo generator-hubot \  
&& useradd hubot -m \  
&& mkdir /home/hubot/app \  
&& chown hubot.hubot /home/hubot/app \  
&& groupadd -g 999999 docker \  
&& usermod -G docker hubot  
  
USER hubot  
  
WORKDIR /home/hubot/app  
  
RUN set -xe \  
&& yo hubot --owner="$HUBOT_OWNER" \  
\--name="$HUBOT_NAME" \  
\--description="$HUBOT_DESCRIPTION" \  
\--adapter="$HUBOT_ADAPTER" \  
\--defaults \  
&& sed -i /heroku/d ./external-scripts.json \  
&& sed -i /redis-brain/d ./external-scripts.json \  
&& npm install hubot-scripts  
  
COPY ./ /home/hubot/app/node_modules/hubot-gitlab-deploy  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN set -xe \  
&& sudo chown -R hubot.hubot /home/hubot/app \  
&& sudo apt-get install -y fabric --force-yes \  
&& sudo apt-get clean \  
&& sudo chmod +x /usr/local/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
CMD bin/hubot -n $HUBOT_NAME -a $HUBOT_ADAPTER  

