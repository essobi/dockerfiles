FROM debian:jessie  
  
# Why are we installing theses packages?  
# git - obvious (SO WE CAN PULL THE SOFTWARES IN CASE CLARIFICATION NEEDED)  
# make - used in jenkins jobs  
# curl - used for installation process  
# bsdtar - used for installation process  
# software-common-properties - required to install add-apt-respository  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository 'deb http://http.debian.net/debian jessie-backports main'
&& \  
apt-get update  
  
RUN apt --no-install-recommends install -y -t jessie-backports openjdk-8-jre-
headless ca-certificates-java  
  
RUN apt-get install -y --fix-missing git make npm m4 curl bsdtar python-pip
wget zip jq gettext && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget https://storage.googleapis.com/golang/go1.6.3.linux-amd64.tar.gz  
RUN tar -C /usr/local -xzf go1.6.3.linux-amd64.tar.gz  
ENV PATH /usr/local/go/bin:$PATH  
  
RUN pip install boto3 awscli  
  
# Install Jenkins 2.67 war  
ADD http://mirrors.jenkins-ci.org/war/2.67/jenkins.war /opt/jenkins.war  
RUN chmod 644 /opt/jenkins.war  
ENV JENKINS_HOME /jenkins  
  
# install packer as /usr/local/bin/packer  
RUN curl
https://releases.hashicorp.com/packer/1.0.0/packer_1.0.0_linux_amd64.zip |
bsdtar -xvf - -C /usr/local/bin packer  
RUN chmod +x /usr/local/bin/packer  
  
RUN curl -sSL https://get.docker.com/ | sh  
RUN curl -L https://github.com/docker/compose/releases/download/1.13.0/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
RUN wget https://github.com/SimpleHQ/semver-tool/archive/1.2.0.tar.gz  
RUN tar -C /tmp -xzf 1.2.0.tar.gz  
RUN cp /tmp/semver-tool-1.2.0/src/semver /usr/local/bin/semver  
  
# Install kubectl  
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl
-s https://storage.googleapis.com/kubernetes-
release/release/stable.txt)/bin/linux/amd64/kubectl  
RUN chmod +x kubectl  
RUN mv kubectl /usr/local/bin/kubectl  
  
# Install kops  
RUN wget https://github.com/kubernetes/kops/releases/download/1.5.3/kops-
linux-amd64 -O /usr/local/bin/kops  
RUN chmod +x /usr/local/bin/kops  
  
# Install MySQL  
RUN apt-get install mysql-client  
  
RUN curl -sL https://sentry.io/get-cli/ | bash  
  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
EXPOSE 8080  
CMD [""]  

