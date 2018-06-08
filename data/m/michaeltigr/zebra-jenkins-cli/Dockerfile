FROM alpine:3.6  
MAINTAINER Alexander Tolstikov <tolstikov@gmail.com>  
  
USER root  
  
# Install base.  
RUN apk add --update --no-cache \  
bash \  
ca-certificates \  
curl \  
openssh \  
openssl \  
openssl-dev \  
procps \  
tar \  
unzip \  
wget \  
&& update-ca-certificates \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Java.  
ENV JAVA_HOME=/usr  
RUN apk add --update --no-cache openjdk8-jre-base \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD jenkins-cli-wrapper.sh /jenkins-cli/jenkins-cli-wrapper.sh  
ADD jenkins-cli.jar /jenkins-cli/jenkins-cli.jar  
  
RUN chmod +x /jenkins-cli/jenkins-cli-wrapper.sh  
  
ENV JENKINS_URL ""  
ENV PRIVATE_KEY "/ssh/id_rsa"  
# SSH config.  
RUN mkdir -p /root/.ssh  
ADD config/ssh /root/.ssh/config  
RUN chmod 600 /root/.ssh/config  

