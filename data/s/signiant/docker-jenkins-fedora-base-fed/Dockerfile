FROM mattdm/fedora:f19  
MAINTAINER devops@signiant.com  
  
# Add our bldmgr user  
ENV BUILD_USER bldmgr  
ENV BUILD_PASS bldmgr  
ENV BUILD_USER_ID 10012  
ENV BUILD_USER_GROUP users  
ENV BUILD_DOCKER_GROUP docker  
ENV BUILD_DOCKER_GROUP_ID 1001  
ENV UMPIRE_VERSION 0.4.4  
# Create the docker group  
RUN groupadd -g $BUILD_DOCKER_GROUP_ID $BUILD_DOCKER_GROUP  
  
RUN adduser -u $BUILD_USER_ID -g $BUILD_USER_GROUP $BUILD_USER  
  
#RUN passwd -f -u $BUILD_USER  
RUN echo $BUILD_USER:$BUILD_PASS |chpasswd  
  
# Add the user to the docker group  
RUN usermod -a -G $BUILD_DOCKER_GROUP $BUILD_USER  
  
# Install a base set of packages from the default repo  
COPY yum-packages.list /tmp/yum.packages.list  
RUN chmod +r /tmp/yum.packages.list  
RUN yum install -y `cat /tmp/yum.packages.list`  
  
# Install subversion, this needs to be done this way as it tries to install a
broken package  
RUN yum install -y --nodeps subversion  
  
# Install Java  
ENV JAVA_VERSION 7u79  
ENV BUILD_VERSION b15  
ENV JAVA_HOME /usr/java/latest  
  
# Downloading Oracle Java  
RUN wget --no-cookies --no-check-certificate --header "Cookie:
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION-$BUILD_VERSION/jdk-$JAVA_VERSION-linux-x64.rpm" -O
/tmp/jdk-7-linux-x64.rpm  
RUN yum -y install /tmp/jdk-7-linux-x64.rpm  
  
RUN rm -f /tmp/jdk-7-linux-x64.rpm  
  
RUN alternatives --install /usr/bin/java jar /usr/java/latest/bin/java 200000  
RUN alternatives --install /usr/bin/javaws javaws /usr/java/latest/bin/javaws
200000  
RUN alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac
200000  
  
# Update npm  
RUN npm install -g npm@latest-2  
  
# Install maven  
ENV MAVEN_VERSION 3.2.1  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
ENV MAVEN_HOME /usr/share/maven  
  
# Install findbugs  
ENV FINDBUGS_VERSION 2.0.3  
RUN curl -fsSL
http://downloads.sourceforge.net/project/findbugs/findbugs/$FINDBUGS_VERSION/findbugs-$FINDBUGS_VERSION.tar.gz
| tar xzf - -C /home/$BUILD_USER  
  
ENV ANT_VERSION 1.9.7  
RUN cd && \  
wget -q http://www.us.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz && \  
tar -xzf apache-ant-${ANT_VERSION}-bin.tar.gz && \  
mv apache-ant-${ANT_VERSION} /usr/local/apache-ant-${ANT_VERSION} && \  
rm apache-ant-${ANT_VERSION}-bin.tar.gz  
RUN sh -c 'echo ANT_HOME=/usr/local/apache-ant-${ANT_VERSION} >>
/etc/environment'  
ENV ANT_HOME /usr/local/apache-ant-${ANT_VERSION}  
  
# Install our required ant libs  
COPY ant-libs/*.jar ${ANT_HOME}/lib/  
RUN chmod 644 ${ANT_HOME}/lib/*.jar  
  
# Install pip  
RUN cd /tmp && \  
wget https://bootstrap.pypa.io/get-pip.py && \  
python2.7 ./get-pip.py  
  
# Install umpire  
RUN pip2.7 install umpire==${UMPIRE_VERSION}  
  
# Create the folder we use for Jenkins workspaces across all nodes  
RUN mkdir -p /var/lib/jenkins  
RUN chown -R $BUILD_USER:$BUILD_USER_GROUP /var/lib/jenkins  
  
# Add in our common jenkins node tools for bldmgr  
COPY jenkins_nodes /home/$BUILD_USER/jenkins_nodes  
  
# Make our build user require no tty  
RUN echo "Defaults:$BUILD_USER !requiretty" >> /etc/sudoers  
  
# Add user to sudoers with NOPASSWD  
RUN echo "$BUILD_USER ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
#Install umpire  
RUN pip install umpire  
  
# Install and configure SSHD (needed by the Jenkins slave-on-demand plugin)  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN sed -ri 's/session required pam_loginuid.so/#session required
pam_loginuid.so/g' /etc/pam.d/sshd  
RUN sed -ri 's/#PermitEmptyPasswords no/PermitEmptyPasswords yes/g'
/etc/ssh/sshd_config  
RUN mkdir -p /home/$BUILD_USER/.ssh  
RUN chown -R $BUILD_USER:$BUILD_USER_GROUP /home/$BUILD_USER  
RUN chmod 700 /home/$BUILD_USER/.ssh  
  
EXPOSE 22  
# This entry will either run this container as a jenkins slave or just start
SSHD  
# If we're using the slave-on-demand, we start with SSH (the default)  
# Default Jenkins Slave Name  
ENV SLAVE_ID FEDORA_NODE  
ENV SLAVE_OS Linux  
  
ADD start.sh /  
RUN chmod 777 /start.sh  
  
CMD ["sh", "/start.sh"]  

