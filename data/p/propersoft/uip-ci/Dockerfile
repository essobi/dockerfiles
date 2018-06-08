FROM jenkins:1.651.2  
MAINTAINER Alpha Hinex <AlphaHinex@gmail.com>  
  
USER root  
  
# Set time zone  
RUN echo "Asia/Shanghai" > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
  
# Install svn and maven  
RUN apt-get update --fix-missing && apt-get install -y subversion maven  
RUN apt-get clean  
  
# Custom maven's settings  
COPY settings.xml /usr/share/maven/conf/settings.xml  
  
# Set shell variables for java installation  
ENV java_version 1.7.0_80  
ENV filename jdk-7u80-linux-x64.tar.gz  
ENV downloadlink http://download.oracle.com/otn-
pub/java/jdk/7u80-b15/$filename  
  
# Download java, accepting the license agreement  
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" -O /tmp/$filename $downloadlink  
  
# Unpack java  
RUN mkdir /opt/java-oracle && tar -zxf /tmp/$filename -C /opt/java-oracle/  
ENV JAVA_HOME /opt/java-oracle/jdk$java_version  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# Configure symbolic links for the java and javac executables  
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000
&& update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac
20000  
  
# Install gradle  
ENV GRADLE_VERSION 2.12  
WORKDIR /usr/bin  
RUN curl -sLO
https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip &&
\  
unzip gradle-${GRADLE_VERSION}-all.zip && \  
ln -s gradle-${GRADLE_VERSION} gradle && \  
rm gradle-${GRADLE_VERSION}-all.zip  
  
ENV GRADLE_HOME /usr/bin/gradle  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
# Install jenkins plugins  
COPY plugins /usr/share/jenkins/plugins  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins  

