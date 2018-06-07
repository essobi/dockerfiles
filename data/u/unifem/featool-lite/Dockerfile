# Builds a Docker image for FEATool-Lite in a Desktop environment  
# with Ubuntu and LXDE.  
#  
# The built image can be found at:  
# https://hub.docker.com/r/unifem/featool-lite  
#  
# Authors:  
# Xiangmin Jiao <xmjiao@gmail.com>  
FROM unifem/desktop-base:latest  
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"  
  
USER root  
WORKDIR /tmp  
  
ADD octaverc $DOCKER_HOME/.octaverc  
  
# Install latest version of octave  
RUN apt-add-repository ppa:octave/stable && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
bsdtar zip unzip \  
build-essential make \  
octave liboctave-dev \  
gnuplot-x11 \  
libopenblas-base libatlas3-base \  
pstoedit octave-info emacs24 && \  
curl -s https://www.featool.com/featool-lite.zip | \  
bsdtar -C $DOCKER_HOME -zxf - && \  
echo "@octave --force-gui" >> $DOCKER_HOME/.config/lxsession/LXDE/autostart &&
\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
chown -R $DOCKER_USER:$DOCKER_USER $DOCKER_HOME  
  
WORKDIR $DOCKER_HOME  

