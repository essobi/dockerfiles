FROM ubuntu:12.04  
MAINTAINER yegor256 "yegor256@gmail.com"  
RUN apt-get update -qq  
  
# Common dependencies  
RUN apt-get install -y sudo  
RUN apt-get install -y git  
RUN apt-get install -y ruby1.9.3  
RUN apt-get install -y s3cmd  
  
# Dependencies to execute android  
RUN apt-get install -y openjdk-7-jdk  
RUN apt-get install -y ia32-libs ia32-libs-multiarch  
  
# Main Android SDK  
RUN apt-get install -y --no-install-recommends wget  
RUN cd /opt && wget -q http://dl.google.com/android/android-sdk_r23-linux.tgz  
RUN cd /opt && tar xzf android-sdk_r23-linux.tgz  
RUN cd /opt && rm -f android-sdk_r23-linux.tgz  
  
# Other tools and resources of Android SDK  
ENV ANDROID_HOME /opt/android-sdk-linux  
ENV PATH ${PATH}:${ANDROID_HOME}/tools:${ANDROID_HOME}/platform-tools  
RUN ( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) | android update sdk
--no-ui --filter build-tools-20.0.0,android-19  
  
# Download and install latest Maven  
ENV MAVEN_MAJOR 3  
ENV MAVEN_VERSION 3.2.3  
ENV MAVEN_OPTS -XX:MaxPermSize=256m -Xmx1g  
RUN wget
http://www.us.apache.org/dist/maven/maven-$MAVEN_MAJOR/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz  
RUN tar -xzf apache-maven-$MAVEN_VERSION-bin.tar.gz -C /usr/local  
RUN mv /usr/local/apache-maven-$MAVEN_VERSION /usr/local/maven  
RUN rm apache-maven-$MAVEN_VERSION-bin.tar.gz  
RUN ln -s /usr/local/maven/bin/mvn /usr/local/bin/mvn  
  
# Warming up Maven local repo  
RUN git clone https://github.com/aintshy/android /tmp/android  
RUN cd /tmp/android && mvn clean install site -Pqulice -Psite --errors  
RUN rm -rf /tmp/android  
  
# Installing PDD  
RUN apt-get install -y libxslt-dev libxml2-dev  
RUN apt-get install -y build-essential  
RUN gem install nokogiri -- --use-system-libraries=true \--with-
xml2-include=/usr/include/libxml2  
RUN apt-get install -y libmagic-dev  
RUN gem install pdd  
  
# Cleaning  
RUN apt-get clean  
  
# Fix permissions  
RUN chown -R root:root /opt/android-sdk-linux  
RUN chmod -R a+rx /opt/android-sdk-linux  

