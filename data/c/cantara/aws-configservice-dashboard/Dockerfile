FROM cantara/alpine-zulu-jdk8  
  
RUN apk add --update \  
groff \  
python \  
python-dev \  
py-pip \  
bash \  
&& pip install awscli awscli-cwlogs boto3 \  
&& rm -rf /var/cache/apk/*  
  
ENV USER=appuser \  
HOME=/home/appuser  
#Builds latest by default, which means it downloads latest jar/snapshot from
mvnrepo  
ARG DOCKER_TAG=latest  
RUN adduser -S $USER  
  
COPY config_override/* $HOME/config_override/  
COPY toRoot/* $HOME/  
RUN if [ $DOCKER_TAG = "latest" ]; then \  
curl -L -o $HOME/app.jar
"http://mvnrepo.cantara.no/service/local/artifact/maven/redirect?r=snapshots&g=no.cantara.csdb&a=ConfigService-
Dashboard&v=LATEST"; \  
else \  
curl -L -o $HOME/app.jar
"http://mvnrepo.cantara.no/content/repositories/releases/no/cantara/csdb/ConfigService-
Dashboard/`echo $DOCKER_TAG | cut -d \\- -f3`/$DOCKER_TAG.jar"; \  
fi  
## Create directory for holding application logs and configure permissions  
## Configure permissions  
RUN mkdir -p $HOME/logs && \  
chmod 755 $HOME/*.sh && \  
chown -R $USER $HOME && \  
ln -s /usr/local/java/bin/java /usr/bin/java  
  
## Map data volume container?  
VOLUME ["$HOME/config_override", "$HOME/logs"]  
  
## Expose application port  
EXPOSE 8087  
USER $USER  
WORKDIR /home/$USER  
CMD ["./runapp.sh"]  

