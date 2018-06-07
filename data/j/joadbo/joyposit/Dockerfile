FROM node:0.12-slim  
MAINTAINER Joy Borsutzki  
#------  
# Umgebungsvariablen  
ENV HUBOT_NAME NTTBOT  
ENV HUBOT_SLACK_TOKEN false  
ENV HUBOT_AUTH_ADMIN myself  
#------  
# Pre-Install  
ADD build/ /opt/  
WORKDIR /opt  
#-----  
# Install  
RUN npm install --production; npm cache clean  
#-----  
# Post-install  
EXPOSE 8080  
VOLUME /opt/scripts  
CMD ["/opt/bin/hubot", "--name", "Doerte"]  
  

