FROM centos:7  
RUN yum -y install git && \  
yum -y install wget && \  
yum -y install sudo && \  
yum -y install make && \  
yum clean all  
  
RUN echo "root:password" | chpasswd  
RUN useradd jenkins  
  
RUN wget -P /opt/ --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" http://download.oracle.com/otn-
pub/java/jdk/8u66-b17/jdk-8u66-linux-x64.tar.gz \  
&& tar xzf /opt/jdk-8u66-linux-x64.tar.gz -C /opt \  
&& rm /opt/jdk-8u66-linux-x64.tar.gz  
  
RUN alternatives --install /usr/bin/java java /opt/jdk1.8.0_66/bin/java 2 \  
&& alternatives --install /usr/bin/jar jar /opt/jdk1.8.0_66/bin/jar 2 \  
&& alternatives --install /usr/bin/javac javac /opt/jdk1.8.0_66/bin/javac 2 \  
&& alternatives --set jar /opt/jdk1.8.0_66/bin/jar \  
&& alternatives --set javac /opt/jdk1.8.0_66/bin/javac  
  
ENV HOME /home/jenkins  
ENV JAVA_HOME /opt/jdk1.8.0_66  
ENV JRE_HOME /opt/jdk1.8.0_66/jre  
ENV JENKINS_REMOTING_VERSION 2.52  
RUN ["java","-version"]  
  
ADD http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.12.linux.bin.tar.gz /  
  
RUN tar -xvzf /doxygen-1.8.12.linux.bin.tar.gz  
  
COPY Makefile doxygen-1.8.12/Makefile  
  
RUN cd doxygen-1.8.12 && make && make install  
  
RUN curl --create-dirs -sSLo
/usr/share/jenkins/remoting-$JENKINS_REMOTING_VERSION.jar http://repo.jenkins-
ci.org/public/org/jenkins-
ci/main/remoting/$JENKINS_REMOTING_VERSION/remoting-$JENKINS_REMOTING_VERSION.jar
\  
&& chmod 755 /usr/share/jenkins  
  
COPY jenkins-slave.sh /usr/local/bin/jenkins-slave.sh  
  
RUN chmod 755 /usr/local/bin/jenkins-slave.sh  
  
ADD https://get.docker.com/builds/Linux/x86_64/docker-1.11.0.tgz /  
  
RUN tar -xvzf /docker-1.11.0.tgz && mv docker/* /usr/bin/  
  
RUN groupadd docker -g 233 \  
&& usermod -a -G docker jenkins \  
&& usermod -a -G wheel jenkins  
  
# Enable passwordless sudo for users under the "sudo" group  
RUN sed -i.bkp -e 's/%wheel\s\\+ALL=(ALL\\(:ALL\\)\?)\s\\+ALL/%wheel
ALL=NOPASSWD:ALL/g' /etc/sudoers  
  
USER jenkins  
  
VOLUME /home/jenkins  
  
ENTRYPOINT ["/usr/local/bin/jenkins-slave.sh"]  

