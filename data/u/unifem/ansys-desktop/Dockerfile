# Builds a Docker image for ANSYS with Ubuntu and LXDE.  
#  
# Authors:  
# Xiangmin Jiao <xmjiao@gmail.com>  
FROM unifem/desktop-base:latest  
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"  
  
USER root  
WORKDIR /tmp  
  
COPY download_ansys /usr/local/share/  
  
RUN ln -s -f /usr/local/ansys_inc / && \  
echo "@/ansys_inc/v180/Framework/bin/Linux64/runwb2" >>
$DOCKER_HOME/.config/lxsession/LXDE/autostart && \  
rm -rf /tmp/* /var/tmp/* && \  
chown -R $DOCKER_USER:$DOCKER_USER $DOCKER_HOME  
  
WORKDIR $DOCKER_HOME  
  
USER root  

