FROM ubuntu:latest  
  
ENV LANG C.UTF-8  
ENV JAVA_HOME /jdk-9  
  
RUN apt-get update && apt-get install -yq \--no-install-recommends \  
ca-certificates \  
wget && \  
wget -O /tmp/jdk.tar.gz -c \--header "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/9+181/jdk-9_linux-x64_bin.tar.gz && \  
tar -xvzf /tmp/jdk.tar.gz -C / && \  
ln -s $JAVA_HOME/bin/java /usr/bin/java && \  
ln -s $JAVA_HOME/bin/javac /usr/bin/javac && \  
ln -s $JAVA_HOME/bin/jshell /usr/bin/jshell && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["jshell"]  

