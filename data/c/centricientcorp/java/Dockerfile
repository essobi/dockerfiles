FROM ubuntu:xenial  
  
MAINTAINER kyle.mcintyre@centricient.com  
  
RUN apt-get update && apt-get install -y wget software-properties-common
python2.7  
RUN wget https://bootstrap.pypa.io/get-pip.py && python2.7 get-pip.py && pip
install requests  
  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb && \  
echo "9af7440986893c904f24c086c50846ddc5a0f24864f5566b747b8f1a17f7fd52 dumb-
init_1.2.0_amd64.deb" | sha256sum -c --status - && \  
dpkg -i dumb-init_1.2.0_amd64.deb  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
COPY local_policy.jar /usr/lib/jvm/java-8-oracle/jre/lib/security/  
COPY US_export_policy.jar /usr/lib/jvm/java-8-oracle/jre/lib/security/  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  

