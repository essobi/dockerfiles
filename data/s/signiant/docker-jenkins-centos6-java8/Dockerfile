FROM signiant/docker-jenkins-centos-base:centos6  
MAINTAINER devops@signiant.com  
  
ENV BUILD_USER bldmgr  
ENV BUILD_USER_GROUP users  
  
# Set the timezone  
RUN sed -ri '/ZONE=/c ZONE="America\/New York"' /etc/sysconfig/clock  
RUN rm -f /etc/localtime && ln -s /usr/share/zoneinfo/America/New_York
/etc/localtime  
  
# Install maven  
ENV MAVEN_VERSION 3.2.1  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
ENV MAVEN_HOME /usr/share/maven  
  
# Install yum packages required for build node  
COPY yum-packages.list /tmp/yum.packages.list  
RUN chmod +r /tmp/yum.packages.list  
RUN yum install -y -q `cat /tmp/yum.packages.list`  
  
# Install Oracle Java (uninstall java7 installed by the base container)  
RUN yum -y erase jdk.x86_64  
  
ENV JAVA_VERSION 8u151  
ENV BUILD_VERSION b12  
ENV JAVA_HOME /usr/java/latest  
ENV JAVA_TMP_FILE /tmp/jdk-8-linux-x64.rpm  
  
# Downloading Oracle Java  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/e758a0de34e24606bca991d704f6dcbf/jdk-$JAVA_VERSION-
linux-x64.rpm" -O $JAVA_TMP_FILE  
RUN yum -y install $JAVA_TMP_FILE  
RUN rm -f $JAVA_TMP_FILE  
  
RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws
200000  
  
# Install jboss  
RUN wget
http://sourceforge.net/projects/jboss/files/JBoss/JBoss-5.1.0.GA/jboss-5.1.0.GA.zip/download
-O /tmp/jboss-5.1.0.GA.zip  
RUN unzip -q /tmp/jboss-5.1.0.GA.zip -d /usr/local  
RUN rm -f /tmp/jboss-5.1.0.GA.zip  
  
# Install Compass  
RUN gem update --system  
RUN gem install compass  
  
# Update node and npm  
RUN npm version && npm install -g npm@${NPM_VERSION} && npm version \  
&& npm install -g bower grunt@0.4 grunt-cli grunt-connect-proxy@0.1.10 n
phantomjs-prebuilt \  
&& npm install -g n  
  
# We have to use this fixed version otherwise we get fatal error: socket hang
up errors  
RUN npm install -g grunt-connect-proxy@0.1.10  
  
# Update version of findbugs  
ENV FINDBUGS_VERSION 3.0.1  
RUN curl -fSLO
http://downloads.sourceforge.net/project/findbugs/findbugs/$FINDBUGS_VERSION/findbugs-
noUpdateChecks-$FINDBUGS_VERSION.tar.gz && \  
tar xzf findbugs-noUpdateChecks-$FINDBUGS_VERSION.tar.gz -C /home/$BUILD_USER
&& \  
rm findbugs-noUpdateChecks-$FINDBUGS_VERSION.tar.gz  
  
# Make sure anything/everything we put in the build user's home dir is owned
correctly  
RUN chown -R $BUILD_USER:$BUILD_USER_GROUP /home/$BUILD_USER  
  
EXPOSE 22  
# This entry will either run this container as a jenkins slave or just start
SSHD  
# If we're using the slave-on-demand, we start with SSH (the default)  
# Default Jenkins Slave Name  
ENV SLAVE_ID JAVA_NODE  
ENV SLAVE_OS Linux  
  
ADD start.sh /  
RUN chmod 777 /start.sh  
  
CMD ["sh", "/start.sh"]  

