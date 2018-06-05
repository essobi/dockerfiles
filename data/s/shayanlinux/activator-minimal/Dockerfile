FROM java:8  
MAINTAINER shayanlinux  
  
ENV ACTIVATOR_VERSION 1.3.9  
RUN apt-get update && \  
apt-get install -yq wget unzip && \  
apt-get autoremove -yq && \  
apt-get clean all  
  
RUN cd /tmp && \  
wget http://downloads.typesafe.com/typesafe-
activator/$ACTIVATOR_VERSION/typesafe-activator-$ACTIVATOR_VERSION-minimal.zip
&& \  
unzip -qq typesafe-activator-$ACTIVATOR_VERSION-minimal.zip && \  
mv /tmp/activator-$ACTIVATOR_VERSION-minimal /opt/activator-$ACTIVATOR_VERSION
&& \  
ln -s /opt/activator-$ACTIVATOR_VERSION/bin/activator /usr/local/bin/activator
&& \  
rm /tmp/typesafe-activator-$ACTIVATOR_VERSION-minimal.zip  
  

