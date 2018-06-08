FROM ubuntu:14.04  
MAINTAINER Evgeny Karataev <Karataev.Evgeny@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
openssh-server \  
curl \  
git \  
software-properties-common  
  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer \  
oracle-java8-set-default  
  
RUN mkdir -p /var/run/sshd  
  
ENV MAVEN_VERSION 3.2.5  
RUN curl -sSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ENV MAVEN_HOME /usr/share/maven  
ENV M2_HOME /usr/share/maven  
ENV M2 $M2_HOME/bin  
  
ENV PATH $M2:$PATH:$JAVA_HOME/bin  
  
ENV CLASSPATH $JAVA_HOME/lib:.  
  
RUN useradd -d /home/query query  
RUN mkdir -p /home/query  
RUN chown query /home/query  
  
RUN echo "query:query" | chpasswd  
  
COPY docker-entrypoint.sh /home/query/entrypoint.sh  
COPY dbinit.sql /home/query/dbinit.sql  
  
RUN chmod -R 777 /home/query  
  
ENTRYPOINT ["/home/query/entrypoint.sh"]  
  
EXPOSE 22  
EXPOSE 7654  
VOLUME /opt/project/deployed  
  
CMD ["/usr/sbin/sshd", "-D"]  

