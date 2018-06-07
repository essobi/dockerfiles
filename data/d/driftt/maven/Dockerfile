FROM driftt/java  
  
# We wanted a maven builder image that is based off of orackle jdk so that we  
# are building with the same jdk with which we run. Thus we copied the maven  
# dockerfile into here after basing of of an oracle jdk  
#  
# From: https://github.com/carlossg/docker-
maven/blob/322d0dff5d0531ccaf47bf49338cb3e294fd66c8/jdk-8/Dockerfile  
RUN apk add --no-cache curl tar bash  
  
ARG MAVEN_VERSION=3.3.9  
ARG USER_HOME_DIR="/root"  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"  
COPY mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh  
COPY settings-docker.xml /usr/share/maven/ref/  
  
VOLUME "$USER_HOME_DIR/.m2"  
  
ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]  
CMD ["mvn"]  
  
#  
# Drift additions from here down  
#  
# Add the src dir as a volume so that we can mount it into this image at run  
# time, thus allowing us to call this image to build and output to the current  
# directory  
#  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
VOLUME /usr/src/app  

