FROM ubuntu:14.04  
MAINTAINER Deukjin Kim <kdalma@kimssoft.com>  
  
  
# Let's start with some basic stuff.  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
wget \  
lxc \  
iptables \  
git \  
vim  
  
# Add ssh client, python 2.7  
RUN apt-get install -y ssh-client \  
python2.7 \  
python2.7-dev \  
&& apt-get autoremove \  
&& apt-get clean  
  
# Install Mysql  
RUN apt-get install -y mysql-server mysql-client \  
&& apt-get autoremove \  
&& apt-get clean  
  
# Install Jenkins  
RUN apt-get install -y software-properties-common python-software-properties \  
&& wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | apt-key
add - \  
&& echo "deb http://pkg.jenkins-ci.org/debian binary/" >
/etc/apt/sources.list.d/jenkins.list \  
&& apt-get update \  
&& apt-get install -y openjdk-7-jre maven \  
zip \  
jenkins  
  
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/jenkins \  
&& chmod 0440 /etc/sudoers.d/jenkins  
  
# Install Docker from Docker Inc. repositories.  
RUN curl -sSL https://get.docker.com/ | sh  
  
# Install the magic wrapper.  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
ADD ./setup.sh /setup.sh  
ADD ./check.sh /check.sh  
ADD ./start.sh /start.sh  
ADD ./jenkins_setting /tmp/jenkins_setting/  
ADD ./jdk-1.8.45.tar.gz /tmp/jdk  
RUN chmod +x /usr/local/bin/wrapdocker  
RUN chmod 755 /setup.sh  
RUN chmod 755 /check.sh  
RUN chmod 755 /start.sh  
  
# Define additional metadata for our image.  
EXPOSE 8080  
EXPOSE 8090  
EXPOSE 8000  
EXPOSE 3306  
VOLUME /var/lib/docker  
VOLUME /develop  
  
CMD ["/start.sh"]  
  

