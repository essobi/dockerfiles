FROM ubuntu:14.04  
RUN apt-get -qq update  
RUN apt-get install -y build-essential python-software-properties software-
properties-common wget curl git fontconfig subversion  
RUN apt-get -qq update  
  
# SSH server  
RUN apt-get install -y openssh-server  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
#Java 1.6  
RUN apt-get install -y openjdk-7-jdk  
  
# Maven 3.2.5  
RUN wget http://apache.petsads.us/maven/maven-3/3.2.5/binaries/apache-
maven-3.2.5-bin.tar.gz  
RUN mkdir -p /opt/maven  
RUN tar -zxf apache-maven-3.2.5-bin.tar.gz -C /opt/maven  
RUN ln -s /opt/maven/apache-maven-3.2.5/bin/mvn /usr/bin  
  
# Set Java and Maven env variables  
ENV M2_HOME /opt/maven/apache-maven-3.2.5  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/  
ENV JAVA_OPTS -Xmx2G -Xms2G -XX:PermSize=256M -XX:MaxPermSize=256m  
  
USER root  
  
# Add user jenkins to the image  
RUN adduser --quiet jenkins  
RUN adduser jenkins sudo  
RUN echo "jenkins:jenkins_docker!" | chpasswd  
  
USER jenkins  
RUN mkdir -p /home/jenkins/.m2/  
COPY settings.xml /home/jenkins/.m2/  
  
USER root  
ENV DISPLAY :10  
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu/  
  
# Standard SSH port  
EXPOSE 22  
# Startup services when running the container  
CMD ["/usr/sbin/sshd -D"]  

