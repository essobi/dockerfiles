FROM delitescere/jdk  
  
MAINTAINER "Daniel Fullarton" <linead@gmail.com>  
  
ENV MAVEN_VERSION 3.3.3  
RUN curl
http://apache.uberglobalmirror.com/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz -o /tmp/maven.tar.gz \  
&& mkdir -p /usr/share/java \  
&& tar xvfz /tmp/maven.tar.gz -C /usr/share/java/ \  
&& mv /usr/share/java/apache-maven-$MAVEN_VERSION /usr/share/java/maven \  
&& rm -rf /tmp/maven.tar.gz \  
&& apk --update add git && rm -rf /var/cache/apk/*  
  
ADD maven.sh /etc/profile.d/maven.sh  
  
RUN adduser -h /var/maven -u 1000 -D -s /bin/bash maven && mkdir -p
/var/maven/.m2/repository && chown -R maven:maven /var/maven/  
  
USER maven  
  
VOLUME ["/app"]  
WORKDIR /app  
  
ENTRYPOINT ["/usr/share/java/maven/bin/mvn"]  

