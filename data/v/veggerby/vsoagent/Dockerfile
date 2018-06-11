FROM node  
MAINTAINER Jesper Veggerby <jesper@veggerby.com>  
  
#env variables  
ENV VSO_CONFIG_USERNAME=""  
ENV VSO_CONFIG_PASSWORD=""  
ENV VSO_CONFIG_URL=""  
ENV VSO_CONFIG_AGENTNAME=$HOSTNAME  
ENV VSO_CONFIG_AGENTPOOL=default  
ENV VSO_CONFIG_SERVICE_USERNAME=vsoservice  
ENV VSO_CONFIG_SERVICE_PASSWORD=vsoservice  
  
RUN apt-get update  
  
# INSTALL Expect  
RUN apt-get install expect -y  
  
# INSTALL GIT  
RUN apt-get install nodejs-legacy -y  
  
# INSTALL VSO Agent  
RUN npm install vsoagent-installer bower gulp -g  
  
#CREATE SOME dirs  
RUN mkdir opt/buildagent  
RUN mkdir opt/buildagent/_work  
  
#COPY expect file  
WORKDIR /opt/buildagent  
COPY ConfigureAgent.expect ConfigureAgent.expect  
  
# Create a service user  
RUN echo
"${VSO_CONFIG_SERVICE_USERNAME}\n${VSO_CONFIG_SERVICE_PASSWORD}\n\n\n\n\n\n\n"
| adduser ${VSO_CONFIG_SERVICE_USERNAME}  
RUN su ${VSO_CONFIG_SERVICE_USERNAME}  
  
# Install the agent  
WORKDIR /opt/buildagent  
RUN vsoagent-installer  
WORKDIR /opt/buildagent/agent  
RUN chown -R ${VSO_CONFIG_SERVICE_USERNAME} /opt/buildagent  
  
WORKDIR /opt/buildagent  
  
USER ${VSO_CONFIG_SERVICE_USERNAME}  
CMD expect ConfigureAgent.expect  

