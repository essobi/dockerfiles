FROM katalonstudio/katalon  
  
# .: Image documentation  
LABEL name="ppadial/katalon-jenkins-slave" \  
maintainer="Paulino Padial <github.com/ppadial>" \  
description="A Jenkins Slave container to run Katalon Tests"  
  
################################################################################  
## PRE-IMAGES CONFIG FOR JENKINS  
## BuildPack :: curl  
RUN apt-get update && apt-get install -y \  
build-essential openssh-server locales git curl wget \  
&& rm -rf /var/lib/apt/lists/*  
################################################################################  
  
################################################################################  
## Configure this image as jenkins-slave  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
# Some environment variables  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Locale generation  
RUN locale-gen en_US.UTF-8  
# Set user jenkins to the image  
RUN useradd -m -d /home/jenkins -s /bin/sh jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
# Configure katalon base image  
COPY xvfb.sh $KATALON_BASE_ROOT_DIR/scripts/xvfb.sh  
RUN chmod +x $KATALON_BASE_ROOT_DIR/index.sh \  
$KATALON_BASE_ROOT_DIR/setup/* \  
$KATALON_BASE_ROOT_DIR/scripts/*  
RUN chmod +x $KATALON_KATALON_ROOT_DIR/index.sh \  
$KATALON_KATALON_ROOT_DIR/setup/* \  
$KATALON_KATALON_ROOT_DIR/scripts/*  
# Copy the bashrc for jenkins user, if not, the env variables are  
# not available for him, just for root  
COPY .bashrc /home/jenkins/.bashrc  
RUN chown -R jenkins:jenkins /home/jenkins/.bashrc $KATALON_ROOT_DIR  
  
# Patch: Setup the default shell to bash  
RUN chsh -s /bin/bash jenkins  
# Standard SSH port  
EXPOSE 22  
  
# Default command  
ENTRYPOINT /usr/sbin/sshd -D  

