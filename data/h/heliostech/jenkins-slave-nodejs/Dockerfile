FROM heliostech/jenkins-slave-java:8  
MAINTAINER Camille Meulien <camille.meulien@gmail.com>  
  
USER root  
#  
# Install groovy  
#  
ENV GROOVY_VERSION=2.4.6 \  
PATH=${PATH}:/opt/groovy/bin  
  
RUN yum install -y bzip2 liberation* dejavu*  
RUN yum install -y unzip \  
&& curl -sSLo apache-groovy-binary-${GROOVY_VERSION}.zip
https://dl.bintray.com/groovy/maven/apache-groovy-binary-${GROOVY_VERSION}.zip
\  
&& unzip apache-groovy-binary-${GROOVY_VERSION}.zip -d /opt/ \  
&& ln -s /opt/groovy-${GROOVY_VERSION} /opt/groovy \  
&& rm -f apache-groovy-binary-${GROOVY_VERSION}.zip  
  
#  
# Install nodejs  
#  
ENV NODE_VERSION=4.4.3 \  
PATH=${PATH}:/opt/nodejs/bin  
  
RUN mkdir /opt/nodejs \  
&& curl
http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
| tar xvzf - -C /opt/nodejs --strip-components=1  
  
USER jenkins-slave  
VOLUME $HOME  

