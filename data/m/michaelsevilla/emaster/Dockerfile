FROM tutum/ubuntu:trusty  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
RUN echo "===> Install the basics..." && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -yq --force-yes \  
apt-transport-https \  
curl \  
git \  
openjdk-7-jre \  
lynx \  
openssh-client \  
software-properties-common \  
vim \  
wget  
  
RUN echo "===> Install Ansible..." && \  
echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" | tee
/etc/apt/sources.list.d/ansible.list && \  
echo "deb-src http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/ansible.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7BB9C367 &&
\  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -yq --force-yes ansible  
  
RUN echo "===> Cleanup apt-get..." && \  
sudo apt-get clean && sudo rm -rf \  
/var/lib/apt/lists/* /etc/apt/sources.list.d/ansible.list \  
tmp/* /var/tmp/*  
  
RUN echo "===> Getting graph utilities..." && \  
wget
https://github.com/adamcrume/TailPlot/releases/download/v1.4.0/tailplot-1.4.0-jar-
with-dependencies.jar && \  
echo "java -Dsun.java2d.opengl=true -jar /tailplot-1.4.0-jar-with-
dependencies.jar \"\$@\"" >> /bin/tailplot && \  
chmod 750 /bin/tailplot  
  
RUN echo "===> Adding hosts and customizing environment..." && \  
echo '[local]\nlocalhost\n' > /etc/ansible/hosts && \  
ssh-keygen -t rsa -N '' -f ~/.ssh/id_rsa && \  
mkdir /root/callbacks  
  
ADD separate_play.py /root/callbacks/separate_play.py  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod 750 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

