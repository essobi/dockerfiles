# Builds a Docker image for COMSOL with Ubuntu and LXDE.  
#  
# Authors:  
# Xiangmin Jiao <xmjiao@gmail.com>  
FROM unifem/desktop-base:latest  
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"  
  
USER root  
WORKDIR /tmp  
  
COPY download_comsol /usr/local/share/  
  
ENV UE_USER=unifem  
  
RUN ln -s -f /usr/local/comsol50/multiphysics/bin/comsol /usr/local/bin && \  
echo "@comsol" >> $DOCKER_HOME/.config/lxsession/LXDE/autostart && \  
rm -rf /tmp/* /var/tmp/* && \  
chown -R $UE_USER:$UE_USER /home/$UE_USER  
  
WORKDIR $DOCKER_HOME  
  
USER root  
ENTRYPOINT ["/sbin/my_init","--
quiet","--","/sbin/setuser","unifem","/bin/bash","-l","-c"]  
CMD ["/bin/bash","-l","-i"]  

