FROM centos:centos6  
  
MAINTAINER Jesus Alvarez @Chuyqa  
  
RUN echo root:changeme | chpasswd  
  
# Build packages  
RUN yum clean all -y && yum update -y  
RUN yum -y install vim wget rpm-build which tar openssh-server openssh-clients
git python-setuptools python-devel glibc-common  
  
ENV HOME /root  
  
#Install JAVA  
RUN wget --no-check-certificate --no-cookies --header
"Cookie:oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/8u60-b27/jdk-8u60-linux-x64.rpm -O
jdk-8u60-linux-x64.rpm  
RUN rpm -Uvh jdk-8u60-linux-x64.rpm  
ENV JAVA_HOME /usr/java/default/  
  
#Install Maven 3.3.0+  
RUN mkdir -p /opt/maven  
WORKDIR /opt/maven  
RUN wget
http://download.nextag.com/apache/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz  
RUN tar -xvzf /opt/maven/apache-maven-3.3.9-bin.tar.gz  
RUN rm -rf /opt/maven/apache-maven-3.3.9-bin.tar.gz  
  
ENV M2_HOME /opt/maven/apache-maven-3.3.9  
ENV MAVEN_OPTS -Xmx2048m  
ENV PATH $PATH:$JAVA_HOME/bin:$M2_HOME/bin  
  
  
# SSH key  
RUN ssh-keygen -f /root/.ssh/id_rsa -t rsa -N ''  
RUN cat /root/.ssh/id_rsa.pub > /root/.ssh/authorized_keys  
RUN chmod 600 /root/.ssh/authorized_keys  
RUN sed -ri 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config  
  
# Clone Ranger  
WORKDIR /tmp  
RUN git clone https://github.com/apache/incubator-ranger  
  
WORKDIR /tmp/incubator-ranger/  
RUN mvn dependency:resolve  

