FROM ubuntu:12.04  
MAINTAINER Niels Freier  
  
ENV WARURL
https://github.com/takezoe/gitbucket/releases/download/2.8/gitbucket.war  
ENV USER gitbucket  
ENV SSHPASS gitbucket  
  
# Run upgrades  
RUN echo deb http://us.archive.ubuntu.com/ubuntu/ precise universe multiverse
>> /etc/apt/sources.list;\  
echo deb http://us.archive.ubuntu.com/ubuntu/ precise-updates main restricted
universe >> /etc/apt/sources.list;\  
echo deb http://security.ubuntu.com/ubuntu precise-security main restricted
universe >> /etc/apt/sources.list;\  
echo udev hold | dpkg --set-selections;\  
echo initscripts hold | dpkg --set-selections;\  
echo upstart hold | dpkg --set-selections;\  
apt-get update;\  
apt-get -y upgrade  
  
# Install ssh and add-apt-repository  
RUN apt-get install -y python-software-properties openssh-server && mkdir
/var/run/sshd  
  
# Install Java  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo yes | apt-get install -y oracle-java7-installer  
  
# Add user  
RUN useradd $USER && adduser $USER sudo && echo "${USER}:${SSHPASS}" |chpasswd
&& mkdir /home/$USER && chown -R $USER /home/$USER && chsh -s /bin/bash $USER  
  
# Install gitbucket  
ADD $WARURL /home/$USER/gitbucket/gitbucket.war  
  
EXPOSE 22  
EXPOSE 8080  
VOLUME ["/data"]  
  
CMD /usr/sbin/sshd && java -jar /home/$USER/gitbucket/gitbucket.war --port
8080 --host 0.0.0.0 --gitbucket.home=/data

