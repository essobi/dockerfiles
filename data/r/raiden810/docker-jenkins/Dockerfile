FROM ubuntu:xenial  
LABEL maintainer "raiden81 <raiden81@gmx.de>"  
  
### Update System  
RUN apt-get update -qq  
RUN apt-get dist-upgrade -y  
  
### important tools  
RUN apt-get install -y sudo apt-utils  
RUN apt-get install -y wget locales  
  
### Environment Installation  
RUN dpkg-reconfigure locales && \  
locale-gen en_US.UTF-8 && \  
/usr/sbin/update-locale LANG=en_US.UTF-8  
  
### Environment variables  
ENV LC_ALL C.UTF-8  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
DEBIAN_FRONTEND='noninteractive'  
### Install Application  
RUN apt-get -y install \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
openjdk-8-jdk \  
software-properties-common && \  
curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID")/gpg | apt-key add - && \  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo
"$ID") \  
$(lsb_release -cs) \  
stable" && \  
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-
key add - && \  
add-apt-repository "deb https://pkg.jenkins.io/debian-stable binary/" && \  
apt-get update && \  
apt-get install -y docker-ce jenkins && \  
usermod -a -G docker jenkins  
  
### Volume  
VOLUME ["/var/lib/jenkins"]  
  
### Expose ports  
EXPOSE 8080 50000  
### Start jenkins  
COPY start.sh /usr/bin/start.sh  
RUN chmod +x /usr/bin/start.sh  
ENTRYPOINT ["/usr/bin/start.sh"]  
CMD ["run"]  

