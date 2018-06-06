# A image with apache-jmeter and plugins (latest version)  
# For more information: https://github.com/devTransition/docker-jmeter-remote-
sshd  
# use ubuntu 16.04 as base  
FROM ubuntu:xenial  
MAINTAINER Nicolas Wild <nwild79@gmail.com>  
  
### env ###  
ENV JMETER_VERSION 3.0  
ENV PLUGINS_VERSION 1.4.0  
ENV JMETER_PATH /srv/var/jmeter  
ENV PLUGINS_PATH $JMETER_PATH/plugins  
  
### base setup ###  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
ENV HOME /root  
# enable universe  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install software-properties-common \  
&& apt-get -y install unzip \  
&& apt-get -y install pwgen  
  
### Install SSHD ###  
RUN apt-get install -y openssh-server \  
&& apt-get install -y pwgen \  
&& mkdir /var/run/sshd \  
&& mkdir /root/.ssh  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
RUN sed -i -e 's/without-password/yes/g' /etc/ssh/sshd_config  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
### Install Jmeter ###  
# Automagically accept Oracle's license (for oracle-java8-installer)  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN add-apt-repository ppa:webupd8team/java \  
&& apt-get update \  
&& apt-get install -y oracle-java8-installer  
  
RUN mkdir -p $JMETER_PATH \  
&& wget -q http://www.eu.apache.org/dist/jmeter/binaries/apache-
jmeter-$JMETER_VERSION.tgz  
  
RUN tar -zxf apache-jmeter-$JMETER_VERSION.tgz --strip-components=1 -C
$JMETER_PATH \  
&& rm apache-jmeter-$JMETER_VERSION.tgz  
  
# Install plugins  
# - JMeterPlugins-Standard  
# - JMeterPlugins-Extras  
# - JMeterPlugins-ExtrasLibs  
RUN mkdir -p $PLUGINS_PATH \  
&& wget -q http://jmeter-plugins.org/downloads/file/JMeterPlugins-
ExtrasLibs-$PLUGINS_VERSION.zip \  
&& ls -la \  
&& ls -la $PLUGINS_PATH \  
&& unzip -o -d $PLUGINS_PATH JMeterPlugins-ExtrasLibs-$PLUGINS_VERSION.zip \  
&& wget -q http://jmeter-plugins.org/downloads/file/JMeterPlugins-
Extras-$PLUGINS_VERSION.zip \  
&& unzip -o -d $PLUGINS_PATH JMeterPlugins-Extras-$PLUGINS_VERSION.zip \  
&& wget -q http://jmeter-plugins.org/downloads/file/JMeterPlugins-
Standard-$PLUGINS_VERSION.zip \  
&& unzip -o -d $PLUGINS_PATH JMeterPlugins-Standard-$PLUGINS_VERSION.zip \  
&& rm *.zip  
  
# Copy plugins to jmeter and cleanup  
RUN cp $PLUGINS_PATH/lib/*.jar $JMETER_PATH/lib/ \  
&& cp $PLUGINS_PATH/lib/ext/*.jar $JMETER_PATH/lib/ext/ \  
&& rm -rf $PLUGINS_PATH  
  
# Clean up when done  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy user.properties  
ADD user.properties $JMETER_PATH/apache-jmeter-$JMETER_VERSION/bin/  
  
ADD run-services.sh /  
RUN chmod a+x /run-services.sh  
  
EXPOSE 22  
CMD ["/run-services.sh"]  

