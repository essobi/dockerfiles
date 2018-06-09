#  
# Features installer.  
#  
# Pull base image.  
FROM ubuntu:12.04  
MAINTAINER Roberto Jimenez totemteleko@gmail.com  
  
# Installing dependencies  
# Install Python-properties  
RUN apt-get update && apt-get install python-software-properties -y  
  
# Install Java.  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-add-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer  
  
# Install Maven.  
RUN apt-get update && apt-get install maven -y  
  
# Install curl.  
RUN apt-get update && apt-get install curl openssh-server sshpass -y  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
## Installing the python tool for ENV variables.  
RUN apt-get -y install python-pip  
  
RUN pip install envtpl  
  
RUN mkdir /servicemix  
RUN cd /servicemix  
RUN curl http://archive.apache.org/dist/servicemix/servicemix-4/4.5.3/apache-
servicemix-4.5.3.tar.gz | tar -xvz  
RUN cp -r apache-servicemix-4.5.3/* /servicemix/  
RUN rm -r apache-servicemix-4.5.3  
  
RUN mkdir /esb  
  
ADD org.apache.karaf.features.cfg /servicemix/etc/  
ADD org.apache.servicemix.nmr.cfg.tpl /esb/  
ADD org.apache.servicemix.jbi.cfg.tpl /esb/  
ADD users.properties.tpl /esb/  
ADD setenv.tpl /esb/  
  
ADD run.sh /esb/  
ADD installer.sh /esb/  
RUN chmod +x /esb/installer.sh  
RUN chmod +x /esb/run.sh  
  
# Expose ports. SSH Port, ESB instance SSH port.  
# EXPOSE 22 8181  
EXPOSE 8101 8181  
CMD /bin/sh -c /esb/run.sh  
  

