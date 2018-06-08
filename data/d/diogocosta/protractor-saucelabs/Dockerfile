FROM debian  
  
MAINTAINER Diogo Costa <diogo.fe.costa@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN alias adduser='useradd' && apt-get update && apt-get install -y wget  
  
# Install Java 8  
RUN apt-get -yy update && echo oracle-java8-installer shared/accepted-oracle-
license-v1-1 select true | /usr/bin/debconf-set-selections  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get update && apt-get install oracle-java8-installer -yy  
  
# Install NodeJS and NPM  
RUN wget -qO- https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -yy nodejs --fix-missing  
  
# Clean Install  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install Protractor  
RUN npm install -g protractor  
  
# The ENTRYPOINT allows you to configure a container that will run as an
executable.  
# Creating the mirror volume of your code in the container.  
ENTRYPOINT ["protractor","automated/src/e2e/conf.js"]  
  
# Creating variables to be received "Ex: --sauceUser --sauceKey"  
CMD ["$1 $2"]  
  

