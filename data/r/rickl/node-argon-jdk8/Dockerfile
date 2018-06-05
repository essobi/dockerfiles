from nodesource/trusty:argon  
  
# Oracle JDK 8 instructions from
https://github.com/dockerfile/java/blob/master/oracle-java8/Dockerfile  
  
RUN \  
npm install -g npm && \  
npm install -g gulp bower && \  
echo '{ "allow_root": true }' > /root/.bowerrc && \  
apt-get update && apt-get install -y software-properties-common libfontconfig
&& \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
WORKDIR /work  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
# official nodesource docker image defaults NODE_ENV to 'production'  
ENV NODE_ENV dev  
  
CMD ["bash"]  
  

