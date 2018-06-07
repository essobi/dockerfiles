FROM node:boron-slim  
  
# auto validate license  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
  
# update repos  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get update  
  
# install java  
RUN apt-get install oracle-java8-installer -y  
RUN apt-get install maven -y  
  
RUN apt-get clean  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# download Java Cryptography Extension  
RUN cd /tmp/ && \  
curl -LO "http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip" -H
'Cookie: oraclelicense=accept-securebackup-cookie' && \  
unzip jce_policy-8.zip && \  
rm jce_policy-8.zip && \  
yes |cp -v /tmp/UnlimitedJCEPolicyJDK8/*.jar $JAVA_HOME/jre/lib/security  
  

