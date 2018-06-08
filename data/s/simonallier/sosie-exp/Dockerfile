FROM debian:jessie  
MAINTAINER simon.allier@gmail.com  
  
RUN apt-get update && \  
apt-get -y install sudo procps wget git  
  
#RUN echo "%sudo ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
#useradd -u 5001 -G users,sudo -d /home/user --shell /bin/bash -m user && \  
#echo "secret\nsecret" | passwd user  
RUN wget \  
\--no-cookies \  
\--no-check-certificate \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
-qO- \  
"http://download.oracle.com/otn-
pub/java/jdk/8u25-b17/jdk-8u25-linux-x64.tar.gz" | sudo tar -zx -C /opt/  
  
ENV JAVA_HOME /opt/jdk1.8.0_25  
RUN echo "export JAVA_HOME=$JAVA_HOME" > /root/.bashrc  
ENV PATH $JAVA_HOME/bin:$PATH  
RUN echo "export PATH=$PATH" >> /root/.bashrc  
  
RUN wget --no-verbose -O /tmp/apache-maven-3.2.3.tar.gz \  
http://archive.apache.org/dist/maven/maven-3/3.2.3/binaries/apache-
maven-3.2.3-bin.tar.gz  
  
RUN mkdir -p /opt/maven  
RUN tar xzf /tmp/apache-maven-3.2.3.tar.gz --strip-components=1 \  
-C /opt/maven  
RUN ln -s /opt/maven/bin/mvn /usr/local/bin  
RUN rm -f /tmp/apache-maven-3.2.3.tar.gz  
  
WORKDIR /root  
  
RUN git clone https://github.com/marcelinorc/junco-provider.git  
WORKDIR /root/junco-provider  
RUN mvn install  
  
WORKDIR /root  
RUN git clone https://github.com/DIVERSIFY-project/sosies-generator.git  
WORKDIR /root/sosies-generator  
RUN git checkout rewrite_ast  
  
RUN mvn package -Dmaven.test.skip=true  

