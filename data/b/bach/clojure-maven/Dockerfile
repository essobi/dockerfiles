from clojure:latest  
  
RUN apt-get update && \  
apt-get install -y wget  
  
ENV MAVEN_VERSION="3.3.9" \  
MAVEN_HOME=/opt/maven  
  
RUN cd /tmp && \  
wget
"http://ftp.unicamp.br/pub/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" && \  
tar xzf /tmp/apache-maven-$MAVEN_VERSION-bin.tar.gz -C /opt/ && \  
ln -s /opt/apache-maven-$MAVEN_VERSION /opt/maven && \  
ln -s /opt/maven/bin/mvn /usr/local/bin && \  
rm -f /tmp/apache-maven-$MAVEN_VERSION.tar.gz  
  
ARG USERNAME=clojure  
ARG USERID=64535  
ARG GROUPID=$USERID  
  
RUN addgroup -gid $GROUPID $USERNAME && \  
adduser --disabled-password --gecos '' -u $USERID \--gid $GROUPID $USERNAME  
  
RUN echo "cleaning up" && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -f /var/cache/apk/*  
  
RUN mkdir -p /home/$USERNAME/project  
WORKDIR /home/$USERNAME/project  
USER $USERNAME  
ENV HOME /home/$USERNAME  
  

