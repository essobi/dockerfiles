#  
# Java Dockerfile  
#  
# https://github.com/tamboraorg/docker/crejava  
#  
# Pull base image.  
FROM tamboraorg/creubuntu:2010.0  
MAINTAINER Michael Kahle <michael.kahle@yahoo.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV INITRD No  
ENV LANG en_US.UTF-8  
ENV JAVA_VERSION 8  
RUN apt-get update && \  
apt-get install --no-install-recommends -y openjdk-$JAVA_VERSION-jre-headless
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /cre && touch /cre/versions.txt && \  
echo "$(date +'%F %R') \t creJava \t $(java -version 2>&1 | grep version)" >>
/cre/versions.txt  
  
CMD ["/usr/bin/java"]

