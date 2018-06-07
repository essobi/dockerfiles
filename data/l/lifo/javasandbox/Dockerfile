FROM debian  
MAINTAINER Nick <cyberdak095@gmail.com>  
  
# add user, set up sudo and passwd  
RUN apt-get update && apt-get install -y sudo \  
&& if ! id docker >/dev/null 2>&1; then adduser docker; fi \  
&& usermod -aG sudo docker \  
&& echo "docker ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# install java  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
| tee -a /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886
\  
&& apt-get update && apt-get install oracle-java8-installer -y  
  
# install inotify-tools  
#RUN apt-get install inotify-tools -y  
# install necessary utilities  
RUN apt-get install -y --fix-missing libgtk-3-* && apt-get clean  
  

