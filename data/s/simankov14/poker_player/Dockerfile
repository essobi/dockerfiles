FROM debian:jessie  
RUN mkdir /home/sergey ;mkdir /home/sergey/bot;  
COPY / /home/sergey/bot/  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >>
/etc/apt/sources.list  
RUN apt-get update;  
RUN apt-get -y upgrade  
RUN apt-get install -y git wget g++ bzip2 cmake make gcc  
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-
Linux-x86_64.sh;  
RUN bash Miniconda2-latest-Linux-x86_64.sh -b;  
RUN /root/miniconda2/bin/conda create -y --name poker  
RUN /root/miniconda2/bin/conda install -n poker -y tensorflow mysql-connector-
python matplotlib  
RUN /bin/bash -c "debconf-set-selections <<< 'mysql-server mysql-
server/root_password password 12345678' "  
RUN /bin/bash -c "debconf-set-selections <<< 'mysql-server mysql-
server/root_password_again password 12345678' "  
RUN apt-get install -y mysql-server  
RUN cd /home/sergey/bot; service mysql restart; mysql -u root -p12345678 -e
'create database poker'; mysql -u root -p12345678 poker < poker.sql;  
RUN mkdir /home/sergey/bot/nn-java-bot/bin  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886  
RUN apt-get update  
RUN apt-get -y install oracle-java8-installer  
RUN apt-get install -y libboost-all-dev cmake subversion  
RUN cd /home/sergey/; git clone https://github.com/Simankov/pokerstove  
RUN mkdir /home/sergey/pokerstove/src/build; cd
/home/sergey/pokerstove/src/build; cmake ..; make  
  

