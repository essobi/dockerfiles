FROM ubuntu:trusty  
MAINTAINER Marc "marc.segura@scality.com"  
#############################################  
# Node environment  
ENV node=4.4.1  
# all the stuff required to access github  
# the branch we want to extract data from  
ENV BRANCH=master  
#personal github access token - not really needed since the repo is public  
#ENV GITHUB_TOKEN=ef5c25178b3f14db4af295bc7346c6992a176c5e  
# repo owner  
ENV OWNER=GiorgioRegni  
ENV REPO=Docker-images  
# Make editors happy  
ENV TERM="xterm-256color"  
#############################################  
# disable interactive mode  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Update packages.  
RUN apt-get -qq -y update  
  
# Software installation  
RUN apt-get -qq -y install build-essential telnet iperf tcpdump atop sysstat
gcc g++ git python-software-properties software-properties-common sudo
supervisor python-setuptools python-dev build-essential wget curl default-jre
maven  
  
# install performance tools  
RUN apt-get -qq -y install valgrind  
  
# Node installation  
ADD http://nodejs.org/dist/v${node}/node-v${node}-linux-x64.tar.gz /  
RUN cd /usr && tar xzf /node-v${node}-linux-x64.tar.gz --strip 1 && rm
/node-v${node}-linux-x64.tar.gz  
RUN npm -g install npm  
# Configure sudo  
RUN sed -i "s/requiretty/\\!requiretty/g" /etc/sudoers  
RUN echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# Add docker support  
RUN apt-get -qq -y install apt-transport-https  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
RUN sh -c "echo deb https://apt.dockerproject.org/repo ubuntu-trusty main >
/etc/apt/sources.list.d/docker.list"  
RUN apt-get -qq -y update  
RUN apt-get -qq -y install docker-engine  
# this is what we should do if the repo was private  
#RUN cd /root && curl -H 'Authorization: token ${GITHUB_TOKEN}' -H 'Accept:
application/vnd.github.v3.raw' -O -L
https://raw.githubusercontent.com/${OWNER}/${REPO}/${BRANCH}/scality/ironman-
base/deployment/hosts.bash  
#RUN cd /root && curl -H 'Authorization: token ${GITHUB_TOKEN}' -H 'Accept:
application/vnd.github.v3.raw' -O -L
https://raw.githubusercontent.com/${OWNER}/${REPO}/${BRANCH}/scality/ironman-
base/deployment/hostsd.bash  
# but the repo is public  
RUN cd /root && curl -O -L
https://raw.githubusercontent.com/${OWNER}/${REPO}/${BRANCH}/scality/ironman-
base/deployment/hosts.bash  
RUN cd /root && curl -O -L
https://raw.githubusercontent.com/${OWNER}/${REPO}/${BRANCH}/scality/ironman-
base/deployment/hostsd.bash  
  
RUN chmod a+rx /root/hosts.bash /root/hostsd.bash  
VOLUME ["/var/run"]  
  
# Create the "ironman" user.  
RUN useradd -ms /bin/bash ironman  
RUN sudo usermod -aG docker ironman  
  
# Add PPAs  
RUN add-apt-repository -y "deb
http://ppa.launchpad.net/bpaquet/zeromq4-trusty/ubuntu trusty main"  
RUN add-apt-repository -y ppa:bpaquet/zeromq4-trusty  
  
# install software from PPAs  
RUN apt-get -qq -y update  
RUN apt-get -qq -y install libzmq1 libzmq-dev  
  
# pip  
RUN easy_install pip  
RUN pip install --upgrade virtualenv  
  
# install java  
RUN apt-get update && apt-get install -y -q default-jdk  
  
# install time  
RUN apt-get install -y -q time  
  
# install editors  
RUN apt-get install -y -q vim nano  
  
# Docker compose  
RUN curl -L https://github.com/docker/compose/releases/download/1.5.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod a+x /usr/local/bin/docker-compose  
  
# Run as the "ironman" user.  
USER ironman  
  
# what do when image starts  
CMD bash  

