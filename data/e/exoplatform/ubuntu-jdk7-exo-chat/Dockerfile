# Dockerizing base image for eXo Platform with:  
#  
# - Libre Office  
# - eXo Platform Community 4.1  
# Build: docker build -t exoplatform/ubuntu-jdk7-exo-chat:1.0.0 .  
#  
# Run: docker run -t -i --name=exo-chat exoplatform/ubuntu-jdk7-exo-chat:1.0.0  
# docker run -d --name=exo-chat exoplatform/ubuntu-jdk7-exo-chat:1.0.0  
# docker run -d --name=exo-chat -p 8080:8080 exoplatform/ubuntu-jdk7-exo-
chat:1.0.0  
FROM exoplatform/ubuntu-jdk7-exo:plf-4.1  
MAINTAINER DROUET Frederic <fdrouet+docker@exoplatform.com>  
  
# Install MongoDB  
USER root  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist
10gen' | sudo tee /etc/apt/sources.list.d/mongodb.list  
RUN apt-get -qq update && \  
apt-get -qq -y install mongodb-org && \  
apt-get -qq -y autoremove && \  
apt-get -qq -y autoclean  
  
# Install eXo Chat add-on  
# FIXME : replace "exo" by ${EXO_USER} when
https://github.com/docker/docker/issues/4909 will be fixed.  
USER exo  
RUN ${EXO_APP_DIR}/current/addon install exo-chat-community:1.0.0  
  
# Overide eXo Platform startup script to start MongoDB before launching eXo  
RUN mv ${EXO_APP_DIR}/current/start_eXo.sh ${EXO_APP_DIR}/current/start_eXo-
ORI.sh  
ADD start_eXo.sh ${EXO_APP_DIR}/current/start_eXo.sh  
USER root  
RUN chmod 775 ${EXO_APP_DIR}/current/start_eXo.sh  
RUN chown -R ${EXO_USER}:${EXO_GROUP} ${EXO_APP_DIR}/current/start_eXo.sh  
  
# INFO: We keep root account as the new start_eXo.sh must launch MongoDB and
then sudo to exo account  

