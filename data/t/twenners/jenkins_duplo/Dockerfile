#Jenkins Image Duplo  
FROM debian  
Maintainer Tobias Wenners  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y wget git  
RUN apt-get clean  
  
RUN echo "Europe/Berlin" > /etc/timezone  
RUN rm /etc/localtime  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
RUN wget --no-verbose -O /tmp/apache-maven-3.5.3.tar.gz
http://ftp.halifax.rwth-aachen.de/apache/maven/maven-3/3.5.3/binaries/apache-
maven-3.5.3-bin.tar.gz  
  
RUN tar xzf /tmp/apache-maven-3.5.3.tar.gz -C /opt/  
RUN ln -s /opt/apache-maven-3.5.3 /opt/maven  
RUN ln -s /opt/maven/bin/mvn /usr/local/bin  
RUN rm -f /tmp/apache-maven-3.5.3.tar.gz  
ENV MAVEN_HOME /opt/maven  
  
ENV java_version 1.8.0_172  
ENV filename jdk-8u172-linux-x64.tar.gz  
ENV downloadlink http://download.oracle.com/otn-
pub/java/jdk/8u172-b11/a58eab1ec242421181065cdc37240b08/$filename  
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" -O /tmp/$filename $downloadlink  
  
RUN mkdir /opt/java-oracle && tar -zxf /tmp/$filename -C /opt/java-oracle/  
RUN rm -f /tmp/jdk-8u172-linux-x64.tar.gz  
ENV JAVA_HOME /opt/java-oracle/jdk$java_version  
ENV PATH $JAVA_HOME/bin:$PATH  
  
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000
&& update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac
20000  
  
RUN wget --no-verbose -O /opt/jenkins.war http://mirrors.jenkins.io/war-
stable/latest/jenkins.war  
RUN chmod 644 /opt/jenkins.war  
ENV JENKINS_HOME /jenkins  
  
ARG http_port=8080  
ARG agent_port=50000  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
EXPOSE ${http_port}  
EXPOSE ${agent_port}  
  
  
CMD [""]  

