FROM centos:centos7.2.1511  
MAINTAINER Tetsurou Ayano (tetsurou.ayano@scsk.jp)  
  
RUN yum -y install yum-plugin-ovl  
RUN yum -y update  
#Install common  
RUN yum -y install wget tar vim git  
  
#Install JDK7  
RUN yum -y install java-1.7.0-openjdk java-1.7.0-openjdk-devel  
  
# Install Maven  
ENV MAVEN_VERSION 3.2.5  
ENV M2_HOME /opt/maven/apache-maven-$MAVEN_VERSION  
RUN mkdir -p $M2_HOME  
RUN wget -O /tmp/apache-maven-$MAVEN_VERSION-bin.tar.gz
http://ftp.kddilabs.jp/infosystems/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz  
RUN cd /opt/maven && tar zxf /tmp/apache-maven-$MAVEN_VERSION-bin.tar.gz  
RUN ln -s $M2_HOME/bin/mvn /usr/bin/mvn  
RUN rm /tmp/apache-maven-$MAVEN_VERSION-bin.tar.gz  
  
# Environment parameters  
RUN mkdir -p /opt/pccbuild  
  
ENV PCC_REPOSITORY https://github.com/primecloud-controller-org/primecloud-
controller.git  
ENV PCC_VERSION 2.7.0  
ENV JAVA_HOME /usr/lib/jvm/jre-1.7.0-openjdk  
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/bin  
  
#choose master branch  
RUN git clone \--depth=1 -b $PCC_VERSION $PCC_REPOSITORY  
  
#pre build for maven dependency  
WORKDIR /primecloud-controller  
RUN git pull  
RUN mvn clean install -Dmvn.test.skip=true  
#RUN mvn dependency:resolve  
# Build PCC  
ADD build.sh /opt/build.sh  
RUN chmod +x /opt/build.sh  
ENTRYPOINT ["/opt/build.sh"]  
  

