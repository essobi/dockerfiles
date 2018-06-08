FROM pangpanglabs/java8  
  
MAINTAINER pangpanglab <pangpanglab@p2shop.cn>  
  
ARG MAVEN_VERSION=3.3.9  
ARG
MAVEN_BIANRY_URL="http://mirrors.cnnic.cn/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz"  
  
RUN mkdir -p /usr/share/maven \  
&& mkdir -p /root/.m2 \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz "$MAVEN_BIANRY_URL" \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
ENV M2_HOME /usr/share/maven  
  
#COPY mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh  
#RUN chmod +x /usr/local/bin/mvn-entrypoint.sh  
ADD settings.xml /root/.m2  
  
WORKDIR /app  
#ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]  
  
CMD ["mvn"]  

