# https://hub.docker.com/_/centos/  
FROM centos:latest  
  
LABEL MAINTAINER Pavel Alexeev <Pahan@Hubbitus.info>  
  
# Separate install to see repo enabled  
RUN yum install -y epel-release  
  
# We don't fair it will be fat - it intended to start faster many times. So,
single download time have no many sence.  
RUN yum install -y \  
ansible \  
docker \  
java-1.8.0-openjdk-devel java-1.8.0-openjdk-headless \  
ruby \  
git \  
iproute \  
postgresql \  
python2-httpie \  
python2*-pip \  
&& yum clean all \  
&& pip2 install docker-compose --upgrade `# unfortunately no rpm in EPEL
repository`  
  
# First attempt workaround of https://gitlab.com/gitlab-org/gitlab-
ce/issues/22299  
RUN sed -i.bak -- "s/OPTIONS='--selinux-enabled --log-
driver=journald.*$/OPTIONS='--selinux-enabled --log-driver=journald --add-
registry docreg.taskdata.work:5000'/" /etc/sysconfig/docker  

