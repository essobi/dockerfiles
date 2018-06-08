# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
#FROM ubuntu:16.04  
FROM selenium/node-chrome:3.8.1-aluminum  
  
MAINTAINER Alban Andrieu "https://github.com/AlbanAndrieu"  
LABEL vendor="NABLA" version="1.1"  
LABEL description="Image used by Nabla products to build Java/Javascript and
CPP\  
this image is running on Ubuntu 16.04."  
  
ARG JENKINS_HOME=${JENKINS_HOME:-/home/jenkins}  
ENV JENKINS_HOME=${JENKINS_HOME}  
  
# Volume can be accessed outside of container  
#VOLUME [${JENKINS_HOME}]  
# No interactive frontend during docker build  
ENV DEBIAN_FRONTEND=noninteractive \  
DEBCONF_NONINTERACTIVE_SEEN=true  
  
ENV WORKDIR $JENKINS_HOME  
ENV WORKSPACE $JENKINS_HOME  
#ENV PATH /tmp/ansible/bin:/sbin:/usr/sbin:/usr/bin:/bin:$PATH  
#ENV LANG en_US.UTF-8  
ENV TERM="xterm-256color"  
# Working dir  
#WORKDIR /home/jenkins  
WORKDIR $JENKINS_HOME  
  
ADD . $WORKDIR/  
  
USER 0  
#USER root  
#COPY --chown=2000:0 . $JENKINS_HOME  
RUN chown -R 2000:0 $JENKINS_HOME  
  
# Install ansible  
ENV BUILD_PACKAGES="python-dev"  
RUN apt-get clean && apt-get -y update && apt-get install -y \  
-o APT::Install-Recommend=false -o APT::Install-Suggests=false \  
$BUILD_PACKAGES git bzip2 zip unzip python-yaml python-jinja2 python-pip
openssh-server rsyslog && pip install ansible==2.4.1.0 \  
&& apt-get install -y ocl-icd-libopencl1 ocl-icd-opencl-dev clinfo numactl
libnuma1 pciutils \  
xz-utils ksh wget tzdata sudo curl lsof \  
scons \  
python3 python3-pip python3-dev \  
openjdk-8-jdk maven \  
net-tools x11-apps  
  
#USER root  
# Add user jenkins to the image  
RUN groupadd -g 2000 docker && \  
adduser --quiet --uid 2000 --gid 2000 --home ${JENKINS_HOME} jenkins && \  
echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers  
# Set password for the jenkins user (you may want to alter this).  
RUN echo "jenkins:jenkins1234" | chpasswd  
  
#===================  
# Timezone settings  
# Possible alternative:
https://github.com/docker/docker/issues/3359#issuecomment-32150214  
#===================  
ENV TZ "UTC"  
RUN echo "${TZ}" > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
# Execute  
RUN ansible-galaxy install -r $WORKDIR/requirements.yml -p $WORKDIR/roles/
--ignore-errors \  
&& ansible-playbook $WORKDIR/jenkins-slave-docker.yml -i $WORKDIR/hosts -c
local  
  
# Install a basic SSH server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
# Clean up APT when done.  
#RUN AUTO_ADDED_PACKAGES=$(apt-mark showauto) \  
#&& apt-get remove --purge -y $BUILD_PACKAGES $AUTO_ADDED_PACKAGES && \  
RUN apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/* \  
&& ifconfig | awk '/inet addr/{print substr($2,6)}' ## Display IP address
(optional)  
  
USER 2000  
# Standard SSH port  
EXPOSE 22  
#ENTRYPOINT ["/etc/init.d/jenkins-swarm-client"]  
#CMD ["/usr/sbin/sshd", "-D"]  
CMD ["/bin/bash"]  
#CMD ["-g", "deamon off;"]  

