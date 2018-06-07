# Builds a base Docker image that all other FEniCS images are  
# built off of (FROM). In this image we control the end user  
# experience, namely; creating the user fenics, setting up the users  
# environment and the default entry point and cmds.  
#  
# Although this image is not used directly by end-users, it can be  
# found at:  
#  
# https://hub.docker.com/r/fenics/base  
#  
# Authors:  
# Jack S. Hale <jack.hale@uni.lu>  
# Garth N. Wells <gnw20@cam.ac.uk>  
# Xiangmin Jiao <xmjiao@gmail.com>  
FROM phusion/baseimage:0.9.21  
LABEL maintainer "Xiangmin Jiao <xmjiao@gmail.com>"  
  
# Get Ubuntu updates, etc.  
USER root  
WORKDIR /tmp  
  
RUN apt-get update && \  
apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \  
apt-get install -y --no-install-recommends \  
sudo \  
locales \  
man \  
bash-completion && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8  
ADD image /  
  
########################################################  
# Customization for user and location  
########################################################  
ENV DOCKER_USER=fenics  
ENV DOCKER_GROUP=$DOCKER_USER \  
DOCKER_HOME=/home/$DOCKER_USER \  
HOME=/home/$DOCKER_USER  
  
# Set up user so that we do not run as root  
# See https://github.com/phusion/baseimage-docker/issues/186  
# Disable forward logging  
# Add script to set up permissions of home directory on myinit  
# Run ldconfig so that /usr/local/lib is in the default search  
# path for the dynamic linker.  
RUN useradd -m -s /bin/bash -G sudo,docker_env $DOCKER_USER && \  
echo "$DOCKER_USER:docker" | chpasswd && \  
echo "$DOCKER_USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
touch /etc/service/syslog-forwarder/down && \  
ldconfig && \  
touch $DOCKER_HOME/.sudo_as_admin_successful && \  
mkdir $DOCKER_HOME/shared && \  
chown -R $DOCKER_USER:$DOCKER_GROUP $DOCKER_HOME  
  
WORKDIR $DOCKER_HOME  
  
USER root  
ENTRYPOINT ["/sbin/my_init","--
quiet","--","/sbin/setuser","fenics","/bin/bash","-l","-c"]  
CMD ["/bin/bash","-l","-i"]  

