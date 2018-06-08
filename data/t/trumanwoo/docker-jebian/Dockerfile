FROM debian:7.8  
MAINTAINER Truman Woo <chunan.woo@gmail.com>  
  
# Update apt source && install necessary tools  
RUN echo "deb http://mirrors.163.com/debian/ stable main" >
/etc/apt/sources.list \  
&& echo "deb-src http://mirrors.163.com/debian/ stable main" >>
/etc/apt/sources.list  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install -y curl  
RUN apt-get install -y unzip  
  
# Install Oracle JRE 8  
ENV JAVA_HOME /usr/jdk1.8.0_31  
  
RUN curl \  
\--silent \  
\--location \  
\--retry 3 \  
\--cacert /etc/ssl/certs/GeoTrust_Global_CA.pem \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-pub/java/jdk/8u31-b13/server-
jre-8u31-linux-x64.tar.gz" \  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s $JAVA_HOME /usr/java \  
&& rm -rf $JAVA_HOME/man  
  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
# Install Scala & SBT  
ENV SCALA_VERSION 2.11.6  
ENV SBT_VERSION 0.13.8  
# Install Scala  
RUN \  
cd /root && \  
curl -o scala-$SCALA_VERSION.tgz
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz &&
\  
tar -xf scala-$SCALA_VERSION.tgz && \  
rm scala-$SCALA_VERSION.tgz && \  
echo >> /root/.bashrc && \  
echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc  
  
# Install sbt  
COPY sbt-launch.jar /usr/local/bin/  
COPY sbt /usr/local/bin/  
  
RUN \  
chmod u+x /usr/local/bin/sbt  
  
# Define work directory  
WORKDIR /  

