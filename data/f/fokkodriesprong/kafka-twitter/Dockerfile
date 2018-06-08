FROM ubuntu:14.04  
MAINTAINER Fokko Driesprong <fokko@driesprong.frl>  
  
ENV VERSION_JAVA 8u66  
ENV VERSION_MAVEN 3.3.9  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
wget \  
git \  
unzip \  
&& apt-get clean  
  
# Java  
RUN cd /tmp/ \  
&& mkdir -p /usr/java/ \  
&& wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" "http://download.oracle.com/otn-
pub/java/jdk/$VERSION_JAVA-b17/jdk-$VERSION_JAVA-linux-x64.tar.gz" \  
&& tar -xzf jdk-$VERSION_JAVA-linux-x64.tar.gz \  
&& mv jdk*/ /usr/java/jdk1.8.0_$VERSION_JAVA/ \  
&& rm jdk-$VERSION_JAVA-linux-x64.tar.gz \  
&& update-alternatives --install /usr/bin/java java
/usr/java/jdk1.8.0_$VERSION_JAVA/bin/java 100 \  
&& update-alternatives --install /usr/bin/jar jar
/usr/java/jdk1.8.0_$VERSION_JAVA/bin/jar 100 \  
&& update-alternatives --install /usr/bin/javac javac
/usr/java/jdk1.8.0_$VERSION_JAVA/bin/javac 100  
  
ADD . /apps/kafka-twitter/  
  
WORKDIR /apps/kafka-twitter/  
  
RUN ./gradlew installApp  
  
CMD ./gradlew run -Pargs="/apps/kafka-twitter/conf/producer.conf"  

