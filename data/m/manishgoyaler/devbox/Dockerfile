# DOCKER-VERSION 1.8.2  
FROM ubuntu:trusty  
MAINTAINER Manish Goyal <manish.goyal@mobilelive.ca>  
  
ENV JAVA_VERSION 8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ENV MAVEN_VERSION 3.3.9  
ENV MAVEN_HOME /usr/share/maven  
ENV PATH "$PATH:$MAVEN_HOME/bin"  
ENV ACTIVATOR_VER 1.3.7  
# install utilities  
RUN apt-get -y install vim git sudo zip bzip2 fontconfig curl  
  
# Install necessary tools  
RUN apt-get install -y nano wget dialog net-tools  
  
# Download and Install Nginx  
RUN apt-get install -y nginx  
  
# install maven  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
# install java8  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \  
apt-get update && \  
echo oracle-java${JAVA_VERSION}-installer shared/accepted-oracle-license-v1-1
select true | sudo /usr/bin/debconf-set-selections && \  
apt-get install -y --force-yes --no-install-recommends oracle-
java${JAVA_VERSION}-installer oracle-java${JAVA_VERSION}-set-default  
  
# install node.js  
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo bash -  
RUN apt-get install -y nodejs python g++ build-essential  
  
# install yeoman bower grunt gulp  
RUN npm install -g yo bower grunt-cli gulp  
  
#installing activator  
RUN cd /opt \  
&& wget http://downloads.typesafe.com/typesafe-
activator/${ACTIVATOR_VER}/typesafe-activator-${ACTIVATOR_VER}.zip \  
&& unzip typesafe-activator-${ACTIVATOR_VER}.zip \  
&& ln -s /opt/activator-dist-${ACTIVATOR_VER} /opt/activator \  
&& rm -f /opt/typesafe-activator-${ACTIVATOR_VER}.zip  
  
ENV PATH "$PATH:/opt/activator"  
#installing cassandra  
RUN echo "deb http://debian.datastax.com/community stable main" | tee -a
/etc/apt/sources.list.d/cassandra.sources.list  
RUN curl -L https://debian.datastax.com/debian/repo_key | apt-key add -  
RUN apt-get update  
RUN apt-get -q -y install dsc30  
RUN apt-get install cassandra-tools ## Optional utilities  
  
# configure the "devbox" user  
RUN groupadd devbox && useradd devbox -s /bin/bash -m -g devbox -G devbox &&
adduser devbox sudo  
RUN echo 'devbox:devbox' |chpasswd  
RUN mkdir -p /home/devbox/workspace  
RUN mkdir -p /home/devbox/cassandra  
RUN mkdir -p /home/devbox/nginx  
ADD start.txt /home/devbox/start.txt  
RUN cd /home && chown -R devbox:devbox /home/devbox  
RUN chmod -R 777 /opt/activator  
  
# clean  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/oracle-
jdk${JAVA_VERSION}-installer  
  
# expose the working directory, the Tomcat port, the BrowserSync ports  
VOLUME ["/home/devbox/workspace"]  
EXPOSE 8080 8443 3000 3001 8888 9000 5080 80 54338 7000 7001 9042  
CMD ["nginx"]  
CMD ["cassandra"]  
CMD ["tail","-f","/home/devbox/start.txt"]  
# CMD ["/opt/activator/activator", "ui"]  

