# DOCKER-VERSION 1.2.0  
FROM ubuntu:14.04  
MAINTAINER Federico Yankelevich <yankedev@exteso.com>  
  
# make sure the package repository is up to date  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list  
RUN apt-get -y update  
  
# install python-software-properties (so you can do add-apt-repository)  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-
properties software-properties-common  
  
# install SSH server so we can connect multiple times to the container  
RUN apt-get -y install openssh-server && mkdir /var/run/sshd  
  
# install oracle java from PPA  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get -y install oracle-java8-installer && apt-get clean  
  
# Set oracle java as the default java  
RUN update-java-alternatives -s java-8-oracle  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc  
  
# install utilities  
RUN apt-get -y install vim git sudo zip bzip2 fontconfig curl  
  
# install maven  
RUN apt-get -y install maven  
  
# install node.js from PPA  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN apt-get update  
RUN apt-get -y install nodejs  
  
# install yeoman  
RUN npm install -g yo  
  
# configure the "bagarino" and "root" users  
RUN echo 'root:bagarino' |chpasswd  
RUN groupadd bagarino && useradd bagarino -s /bin/bash -m -g bagarino -G
bagarino && adduser bagarino sudo  
RUN echo 'bagarino:bagarino' |chpasswd  
  
#clone source code and execute maven  
#Note: docker build use aggressive caching and thus never really clone repo.
It reuse data from cache from the first clone.  
RUN cd /home/bagarino && \  
git clone https://github.com/exteso/bagarino workspace  
  
RUN cd /home && chown -R bagarino:bagarino /home/bagarino  
RUN cd /home/bagarino/workspace && mvn clean install  
#RUN cd /home/bagarino/workspace && mvn dependency:go-offline  
RUN cd /home && chown -R bagarino:bagarino /home/bagarino  
  
#Add and execute git pull in a script with always-changing-filename to skip
the cache  
ENV VARIABLE update-1414606998.sh  
ADD update.sh $VARIABLE  
RUN /bin/sh $VARIABLE  
  
#Re-execute maven to download new dependencies and check install goes fine  
#RUN cd /home/bagarino/workspace && npm install  
RUN cd /home && chown -R bagarino:bagarino /home/bagarino  
RUN cd /home/bagarino/workspace && mvn clean install  
RUN cd /home && chown -R bagarino:bagarino /home/bagarino  
  
# expose the working directory, the Tomcat port, the Grunt server port,
livereload port, the SSHD port, and run SSHD  
VOLUME ["/bagarino-volume"]  
EXPOSE 8080  
EXPOSE 9000  
EXPOSE 35729  
EXPOSE 22  
CMD /usr/sbin/sshd -D  
CMD cd /home/bagarino/workspace && mvn jetty:run -Pdocker-test  

