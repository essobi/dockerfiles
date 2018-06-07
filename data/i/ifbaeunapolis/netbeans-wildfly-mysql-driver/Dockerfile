FROM ubuntu:14.04  
MAINTAINER Huggo Oliveira "huggo.oliveira1@gmail.com"  
USER root  
#instal unzip && axel && x11 serve Installation && git && firefox  
RUN apt-get update && apt-get install -q -y axel unzip xorg git firefox  
  
# Install Java 8  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -q -y
software-properties-common  
RUN apt-add-repository ppa:webupd8team/java -y  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install oracle-
java8-installer -y && apt-get clean  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
#install wildfly 9.0.2  
#RUN adduser --disabled-password --home /opt/jboss --gecos "" jboss  
# Set the working directory to jboss' user home directory  
WORKDIR /opt/jboss  
  
# Specify the user which should be used to execute all commands below  
#USER jboss  
# Set the WILDFLY_VERSION env variable  
ENV WILDFLY_VERSION 9.0.2.Final  
  
ENV DOWNLOAD_URL=http://download.jboss.org/wildfly/$WILDFLY_VERSION  
  
RUN wget ${DOWNLOAD_URL}/wildfly-$WILDFLY_VERSION.tar.gz  
RUN tar -xf wildfly-$WILDFLY_VERSION.tar.gz  
RUN rm wildfly-$WILDFLY_VERSION.tar.gz  
RUN ln -s wildfly-$WILDFLY_VERSION wildfly  
  
# Set the JBOSS_HOME env variable  
ENV JBOSS_HOME /opt/jboss/wildfly  
  
# add management user (username: admin, passwd: wildfly)  
RUN /opt/jboss/wildfly/bin/add-user.sh admin wildfly --silent  
  
EXPOSE 8080 9990  
#install netbeans  
RUN axel
http://download.netbeans.org/netbeans/8.1/final/zip/moduleclusters/netbeans-8.1-201510222201-all-
in-one.zip  
RUN unzip netbeans-8.1-201510222201-all-in-one.zip  
  
#push project SADE IFBA Eunapolis-BA  
RUN mkdir /root/NetBeansProjects  
RUN cd /root/NetBeansProjects && git clone
https://github.com/IFBAEunapolis/SADE.git  
  
CMD /opt/jboss/netbeans/bin/netbeans  

