FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y python-dev python-pip wget  
RUN pip install awscli  
  
RUN apt-get install -y wget  
ENV JAVA_VERSION=8 \  
JAVA_UPDATE=131 \  
JAVA_BUILD=11 \  
JAVA_TOKEN=d54c1d3a095b4ff2b6607d096fa80163 \  
JAVA_HOME=/usr/lib/jvm/current-java  
  
RUN wget --header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/${JAVA_TOKEN}/jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz"  
RUN tar xzf "jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz"  
RUN mkdir -p /usr/lib/jvm  
RUN mv "jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}"
"/usr/lib/jvm/java-${JAVA_VERSION}-oracle"  
RUN ln -s "java-${JAVA_VERSION}-oracle" $JAVA_HOME  
RUN ln -s $JAVA_HOME/bin/java /usr/bin/java  
RUN rm -rf $JAVA_HOME/*.txt  
RUN rm -rf $JAVA_HOME/*.html  

