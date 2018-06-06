FROM centos:latest  
  
MAINTAINER cousins <bkasodariya@gmail.com>  
  
ENV MAVEN_VERSION 3.3.9  
ENV JAVA_HOME=/usr/java/jdk1.8.0_131/  
  
RUN yum update -y  
  
RUN yum install -y wget && wget -c --header "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.rpm  
  
RUN rpm -ivh jdk-8u131-linux-x64.rpm && rm jdk-8u131-linux-x64.rpm  
  
RUN yum -y install openssh openssh-server openssh-clients openssl-libs  
  
RUN yum -y install rsync  
  
RUN yum update -y && yum install -y unzip  
  
RUN yum -y install epel-release  
  
RUN yum -y install nodejs npm; yum clean all  
  
RUN curl -O https://downloads.typesafe.com/typesafe-activator/1.3.12/typesafe-
activator-1.3.12.zip  
  
RUN unzip typesafe-activator-1.3.12.zip -d / && rm typesafe-
activator-1.3.12.zip && chmod a+x /activator-dist-1.3.12/bin/activator  
  
ENV PATH $PATH:/activator-dist-1.3.12/bin  
  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
EXPOSE 9000 8888  
RUN mkdir /app  
  
WORKDIR /app  
  
CMD ["activator", "run","mvn"]

