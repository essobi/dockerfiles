FROM bradegler/base  
MAINTAINER Brad Egler "begler@gmail.com"  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu precise
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get update  
RUN apt-get -yq install oracle-java7-installer oracle-java7-set-default  
  
CMD ["/bin/bash"]

