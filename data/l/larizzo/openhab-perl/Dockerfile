FROM ubuntu:14.04  
MAINTAINER shawn.rizzoli@larizzo.net  
  
ENV OPENHAB_VERSION=1.8.3  
ENV OPENHAB_DIR=/opt/openhab  
ENV BINDINGS_DIR=/opt/openhab-all-bindings  
ENV DESIGNER_DIR=/opt/openhab-designer  
ENV HABMIN_DIR=$OPENHAB_DIR/webapps/habmin  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# Initial update and install of dependency that can add apt-repos  
RUN apt-get -y update && apt-get install -y software-properties-common python-
software-properties  
  
# Add global apt repos  
RUN add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu precise
universe" && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu precise main
restricted universe multiverse" && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu precise-updates
main restricted universe multiverse" && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu precise-backports
main restricted universe multiverse" && \  
add-apt-repository -y ppa:webupd8team/java  
  
# Install  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget hping3 perl liblwp-
protocol-https-perl libjson-perl libgetopt-long-descriptive-perl  
  
# Install oracle-java8  
RUN (echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections) && apt-get install -y oracle-
java8-installer oracle-java8-set-default  
  
# Cleanup  
RUN rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/*  
  
# Install OpenHAB  
RUN mkdir -p $OPENHAB_DIR \  
&& wget
https://bintray.com/artifact/download/openhab/bin/distribution-$OPENHAB_VERSION-
runtime.zip \  
&& unzip distribution-$OPENHAB_VERSION-runtime.zip -d $OPENHAB_DIR \  
&& rm distribution-$OPENHAB_VERSION-runtime.zip \  
&& mkdir -p $OPENHAB_DIR/logs  
  
# Extract Bindings  
RUN mkdir -p $BINDINGS_DIR \  
&& wget
https://bintray.com/artifact/download/openhab/bin/distribution-$OPENHAB_VERSION-
addons.zip \  
&& unzip distribution-$OPENHAB_VERSION-addons.zip -d $BINDINGS_DIR \  
&& rm distribution-$OPENHAB_VERSION-addons.zip  
  
# Install OpenHAB Designer Linux which can be started via X11  
#RUN mkdir -p $DESIGNER_DIR \  
# && wget
https://bintray.com/artifact/download/openhab/bin/distribution-$OPENHAB_VERSION-
designer-linux64bit.zip \  
# && unzip distribution-$OPENHAB_VERSION-designer-linux64bit.zip -d
$DESIGNER_DIR \  
# && rm distribution-$OPENHAB_VERSION-designer-linux64bit.zip  
# Install HabMin  
RUN mkdir -p $HABMIN_DIR \  
&& wget https://github.com/cdjackson/HABmin/archive/master.zip \  
&& unzip master.zip \  
&& mv HABmin-master/* $HABMIN_DIR \  
&& rm -r HABmin-master master.zip \  
&& mv $HABMIN_DIR/addons/*.jar $OPENHAB_DIR/addons  
  
COPY files/ /opt/  
RUN chmod +x /opt/*.sh  
  
CMD ["/opt/start-openhab-docker.sh"]  
EXPOSE 8080  

