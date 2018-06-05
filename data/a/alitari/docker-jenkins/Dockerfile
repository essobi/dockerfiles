FROM rangalo/java7  
MAINTAINER Alexander Krieg  
  
# Make sure the package repository is up to date.  
RUN echo "deb http://ppa.launchpad.net/natecarlson/maven3/ubuntu precise main"
>> /etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/natecarlson/maven3/ubuntu precise
main" >> /etc/apt/sources.list  
  
RUN apt-get update  
  
# Install a basic SSH server  
RUN apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd  
  
# Install JDK 7 (latest edition)  
#RUN apt-get install -y --no-install-recommends openjdk-7-jdk  
# Install packages needed for the build  
RUN apt-get install -y --force-yes --no-install-recommends git maven3  
ENV MAVEN_HOME /usr/share/maven3  
RUN ln -s /usr/share/maven3/bin/mvn /usr/bin/mvn  
  
# Add user jenkins to the image  
RUN adduser --quiet jenkins  
# Set password for the jenkins user (you may want to alter this).  
RUN echo "jenkins:jenkins" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
# Volume for docker certs  
VOLUME /home/jenkins/.docker  
  
CMD ["/usr/sbin/sshd", "-D"]  

