FROM node:7-alpine  
MAINTAINER 3stadt <docker@3stadt.com>  
ENV REFRESHED_AT 2017-05-30_01  
  
RUN apk update && apk upgrade \  
&& apk add --no-cache git openssh \  
&& addgroup -S discordirc \  
&& adduser -S -g discordirc discordirc \  
&& mkdir -p /home/discordirc/app\  
&& chown -R discordirc:discordirc /home/discordirc  
USER discordirc  
WORKDIR /home/discordirc/app  
RUN git clone https://github.com/reactiflux/discord-irc.git . \  
&& git checkout tags/2.3.0 \  
&& git branch -D master \  
&& npm install && npm run build \  
&& mkdir /home/discordirc/config  
  
CMD []  
ENTRYPOINT ["npm", "start", "--", "--config",
"/home/discordirc/config/config.json"]  

