FROM nlesc/xenon-phusion-base  
MAINTAINER Stefan Verhoeven "s.verhoeven@esciencecenter.nl"  
# Instal Oracle jdk8 + docker  
RUN apt-get update && apt-get install -y python-software-properties && \  
add-apt-repository ppa:webupd8team/java -y && \  
add-apt-repository -y "deb http://archive.ubuntu.com/ubuntu $(lsb_release -sc)
main universe" &&\  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable" && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get install -y docker-ce oracle-java8-installer oracle-java8-set-default
expect && \  
apt-get install -y krb5-user krb5-config && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
# Install docker compose  
curl -L https://github.com/docker/compose/releases/download/1.14.0/docker-
compose-`uname -s`-`uname -m` > /usr/bin/docker-compose && \  
chmod +x /usr/bin/docker-compose && \  
mkdir /code && mkdir -p /etc/my_init.d && \  
# Disable sshd, not needed  
touch /etc/service/sshd/down && \  
usermod -aG docker xenon  
  
COPY krb5.conf /etc/krb5.conf  
  
# ssh keys are already installed in base image, config is needed by Xenon  
RUN setuser xenon touch /home/xenon/.ssh/config  
  
# Tests will be run by xenon user which has uid taken from MYUID environment
var  
ENV MYUID 1000  
ADD entrypoint.sh /bin/entrypoint.sh  
ADD ssh-fillpass-xenon /bin/ssh-fillpass-xenon  
  
VOLUME ["/code"]  
WORKDIR /code  
  
ENTRYPOINT ["/bin/entrypoint.sh"]  
  
CMD ["./gradlew", "--no-daemon", "fixedClientEnvironmentTest"]  

