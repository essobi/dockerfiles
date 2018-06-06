FROM cantara/alpine-zulu-jdk8  
  
RUN apk add --update \  
groff \  
python \  
python-dev \  
py-pip \  
bash \  
&& pip install awscli boto3 \  
&& pip install --upgrade awscli \  
&& rm -rf /var/cache/apk/*  
  
ENV USER=appuser  
ENV HOME=/home/$USER  
RUN adduser -S $USER  
  
#Builds latest by default, which means it downloads latest jar/snapshot from
mvnrepo  
ARG DOCKER_TAG=latest  
  
COPY config_override/* $HOME/config_override/  
COPY toRoot/* $HOME/  
  
RUN if [ $DOCKER_TAG = "latest" ]; then \  
curl -L -o $HOME/app.jar
"https://mvnrepo.cantara.no/service/local/artifact/maven/redirect?r=snapshots&g=no.cantara.jau&a=configservice&v=LATEST";
\  
else \  
curl -L -o $HOME/app.jar
"https://mvnrepo.cantara.no/content/repositories/releases/no/cantara/jau/configservice/$(echo
$DOCKER_TAG | awk -F 'configservice-' '{print $2}')/$DOCKER_TAG.jar"; \  
fi  
  
## Create directory for holding application logs and configure permissions  
## Configure permissions  
RUN mkdir -p $HOME/logs && \  
mkdir -p $HOME/db && \  
chmod 755 $HOME/*.sh && \  
chown -R $USER $HOME  
  
## Map data volume container  
VOLUME ["$HOME/config_override", "$HOME/logs", "$HOME/db"]  
  
## Expose application port  
EXPOSE 8086  
USER $USER  
WORKDIR /home/$USER  
CMD ["./runapp.sh"]

