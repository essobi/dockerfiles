FROM debian:jessie  
USER root  
  
RUN apt-get update && apt-get install -y wget curl git bzip2  
  
# Install Oracle JDK 8u114  
  
RUN cd /tmp && \  
wget \--no-check-certificate -c --header "Cookie: oraclelicense=accept-
securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.tar.gz
&& \  
mkdir /srv/java && \  
tar xf jdk-8u151-linux-x64.tar.gz -C /srv/java && \  
rm -f jdk-8u151-linux-x64.tar.gz && \  
ln -s /srv/java/jdk* /srv/java/jdk && \  
ln -s /srv/java/jdk /srv/java/jvm  
  
# Define commonly used JAVA_HOME variable  
# Add /srv/java and jdk on PATH variable  
  
ENV JAVA_HOME=/srv/java/jdk \  
PATH=${PATH}:/srv/java/jdk/bin:/srv/java  
  
# Install Maven  
  
ENV MAVEN_VERSION 3.3.9  
ENV MAVEN_ROOT /var/lib/maven  
ENV MAVEN_HOME $MAVEN_ROOT/apache-maven-$MAVEN_VERSION  
ENV MAVEN_OPTS -Xms256m -Xmx512m  
  
RUN echo "# Installing Maven " && echo ${MAVEN_VERSION} && \  
wget \--no-verbose -O /tmp/apache-maven-$MAVEN_VERSION.tar.gz \  
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz && \  
mkdir -p $MAVEN_ROOT && \  
tar xzf /tmp/apache-maven-$MAVEN_VERSION.tar.gz -C $MAVEN_ROOT && \  
ln -s $MAVEN_HOME/bin/mvn /usr/local/bin && \  
rm -f /tmp/apache-maven-$MAVEN_VERSION.tar.gz  
  
# Install NodeJS  
  
RUN echo "# Installing NodeJS v5.11.1" && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs  
  
# Install Yarn  
  
RUN apt-get update && apt-get install -y curl apt-transport-https && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn  
  
RUN npm install -g phantomjs  

