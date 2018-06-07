#FROM debian:jessie  
#Maintainer serenedocker  
#Run apt-get update  
#Run apt-get install -y curl wget grep  
#  
## Install Java  
#RUN \  
#echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
#echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >
/etc/apt/sources.list.d/webupd8team-java.list && \  
#echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main"
>> /etc/apt/sources.list.d/webupd8team-java.list && \  
#apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \  
#apt-get update && \  
#apt-get install -y oracle-java8-installer  
#  
## Define commonly used JAVA_HOME variable  
#ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
FROM java:8-jre  
  
Maintainer serenedocker  
Run apt-get update  
Run apt-get install -y curl wget grep  
  
# Set the WILDFLY_VERSION env variable  
#ENV WILDFLY_VERSION 9.0.1.Final  
ENV WILDFLY_VERSION 10.0.0.CR3  
ENV WILDFLY_SHA1 abe037d5d1cb97b4d07fbfe59b6a1345a39a9ae5  
ENV JBOSS_HOME /opt/jboss/wildfly  
# Add the WildFly distribution to /opt, and make wildfly the owner of the
extracted tar content  
# Make sure the distribution is available from a well-known place  
RUN mkdir /opt/jboss  
RUN cd /tmp  
  
RUN curl -O
https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz  
#RUN sha1sum wildfly-$WILDFLY_VERSION.tar.gz | grep $WILDFLY_SHA1  
RUN tar xf wildfly-$WILDFLY_VERSION.tar.gz  
RUN mv wildfly-$WILDFLY_VERSION $JBOSS_HOME  
RUN rm wildfly-$WILDFLY_VERSION.tar.gz  
RUN /opt/jboss/wildfly/bin/add-user.sh serene pw --silent  
# Ensure signals are forwarded to the JVM process correctly for graceful
shutdown  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
COPY ./mysql-connector-java-5.1.37.jar
/opt/jboss/wildfly/standalone/deployments/  
# Expose the ports we're interested in  
EXPOSE 8080  
EXPOSE 9990  
EXPOSE 9090  
# Set the default command to run on boot  
# This will boot WildFly in the standalone mode and bind to all interface  
# Spark  
RUN \  
cd / && \  
wget http://apache.lauf-forum.at/spark/spark-1.5.1/spark-1.5.1-bin-
hadoop2.6.tgz && \  
tar -xvzf spark-1.5.1-bin-hadoop2.6.tgz  
Run rm spark-1.5.1-bin-hadoop2.6.tgz && \  
mv spark* spark  
  
#CMD bash  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b",
"0.0.0.0","-bmanagement","0.0.0.0"]  

