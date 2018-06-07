FROM fvigotti/env-fatubuntu  
  
ENV JDK_VERSION 8u77  
ENV BNUMBER b03  
  
RUN apt-get update \  
&& apt-get install -y wget openssl ca-certificates \  
&& cd /tmp \  
&& wget -qO jdk8.tar.gz \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JDK_VERSION}-${BNUMBER}/jdk-${JDK_VERSION}-linux-x64.tar.gz \  
&& tar xzf jdk8.tar.gz -C /opt \  
&& mv /opt/jdk* /opt/java \  
&& rm /tmp/jdk8.tar.gz \  
&& update-alternatives \--install /usr/bin/java java /opt/java/bin/java 100 \  
&& update-alternatives \--install /usr/bin/javac javac /opt/java/bin/javac 100  
  
# Define working directory  
WORKDIR /root  
#ENTRYPOINT ["java", "-jar", "/whatever/your.jar"]  

