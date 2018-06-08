FROM ubuntu:xenial  
MAINTAINER Deepak Nadig Anantha <deepnadig@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
apt-get install -y software-properties-common && \  
apt-add-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y python maven git curl oracle-java8-installer oracle-
java8-set-default  
#~ apt-get remove --purge -y `apt-mark showauto` && \  
#~ apt-get clean && apt-get purge -y && apt-get autoremove -y  
# Set the environment variables  
ENV HOME /root  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV ONOS_ROOT /root/onos  
ENV KARAF_VERSION 3.0.5  
ENV KARAF_ROOT /root/onos/apache-karaf-3.0.5  
ENV KARAF_LOG /root/onos/apache-karaf-3.0.5/data/log/karaf.log  
ENV BUILD_NUMBER docker  
ENV PATH $PATH:$KARAF_ROOT/bin  
  
#Download and Build ONOS  
WORKDIR /root  
  
RUN git clone https://github.com/opennetworkinglab/onos.git && \  
cd onos && \  
mkdir -p /root/Downloads && \  
mvn clean install && \  
tools/build/onos-package  
  
  
# Ports  
# 6653 - OpenFlow  
# 8181 - GUI  
# 8101 - ONOS CLI  
# 9876 - ONOS CLUSTER COMMUNICATION  
EXPOSE 6653 8181 8101 9876  
# Update ONOS ENV variables and bash profile  
WORKDIR /root  
RUN /bin/bash -c 'cat onos/tools/dev/bash_profile >> .bashrc ;'  
RUN /bin/bash -c 'echo ONOS_IP="$(hostname --ip-address)" >> .bashrc ; echo
$ONOS_IP ;'  
RUN /bin/bash -c 'source $HOME/.bashrc ; tail -1 .bashrc ;'  
  
# Install net-tools as running ONOS locally requires ifconfig  
RUN apt-get install net-tools && \  
apt-get clean && apt-get purge -y && apt-get autoremove -y  
  
# Run ONOS locally on the development container  
#~ RUN /bin/bash -c '/root/onos/tools/dev/bin/onos-karaf clean'  

