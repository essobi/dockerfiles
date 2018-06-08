FROM debian:jessie  
  
ENV JAVA_VERSION "8u162"  
ENV BUILD_VERSION "b12"  
ENV JDK_VERSION "1.8.0_162"  
  
RUN apt-get update && apt-get install -y \  
wget \  
curl \  
&& apt-get install -y --no-install-recommends cron \  
&& mkdir -p /usr/lib/jvm \  
&& cd /usr/lib/jvm \  
&& wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-
securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jdk/8u162-b12/0da788060d494f5095bf8624735fa2f1/server-
jre-8u162-linux-x64.tar.gz" \  
&& tar -zxvf server-jre-${JAVA_VERSION}-linux-x64.tar.gz \  
&& rm /usr/lib/jvm/server-jre-${JAVA_VERSION}-linux-x64.tar.gz \  
&& ln -s /usr/lib/jvm/jdk${JDK_VERSION}/bin/java /bin/ \  
&& cd /usr/lib/jvm/jdk${JDK_VERSION} \  
&& find . -type f -name '*.html' -delete \  
&& find . -type f -name '*.bat' -delete \  
&& find . -type f -name 'COPYRIGHT' -delete \  
&& find . -type f -name 'LICENSE' -delete \  
&& find . -type f -name 'THIRDPARTYLICENSEREADME.txt' -delete \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /var/java-code  
  
VOLUME ["/var/java-code", "/etc/cron.d"]  
  
CMD ["cron", "-f"]  

