FROM ubuntu:14.04.4  
MAINTAINER k_tei@geishatokyo.com  
  
# Install and configure a basic SSH server  
RUN apt-get update &&\  
apt-get install -y openssh-server &&\  
sed -i 's|session required pam_loginuid.so|session optional pam_loginuid.so|g'
/etc/pam.d/sshd &&\  
mkdir -p /var/run/sshd  
  
# Install JDK 7 (latest edition)  
RUN apt-get install -y openjdk-7-jdk  
  
# Install gcc, package  
RUN apt-get install -y autoconf bison build-essential libssl-dev \  
libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev \  
libgdbm3 libgdbm-dev libmysqld-dev wget git curl zip  
  
# Clean  
RUN apt-get clean -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Set locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Set user jenkins to the image  
RUN adduser --quiet jenkins &&\  
echo "jenkins:jenkins" | chpasswd  
  
RUN echo "export LANG=en_US.UTF-8" > /home/jenkins/.profile  
  
RUN mkdir -p /home/jenkins/.sbt/launchers/0.13.8/ &&\  
wget -O /home/jenkins/.sbt/launchers/0.13.8/sbt-launch.jar
https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/0.13.8/sbt-launch.jar  
  
RUN mkdir -p /home/jenkins/.sbt/launchers/0.13.7/ &&\  
wget -O /home/jenkins/.sbt/launchers/0.13.7/sbt-launch.jar
https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/0.13.7/sbt-launch.jar  
  
RUN mkdir -p /home/jenkins/.sbt/launchers/0.13.5/ &&\  
wget -O /home/jenkins/.sbt/launchers/0.13.5/sbt-launch.jar
https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/0.13.5/sbt-launch.jar  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

