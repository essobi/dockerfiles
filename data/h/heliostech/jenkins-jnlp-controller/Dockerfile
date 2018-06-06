FROM debian  
  
MAINTAINER Camille Meulien <camille.meulien@gmail.com>  
  
COPY entrypoint.sh /usr/bin/  
RUN chmod 755 /usr/bin/entrypoint.sh  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
  
#  
# Install remoting jar  
#  
ARG JENKINS_REMOTING_VERSION=2.62.4  
RUN apt-get update \  
&& apt-get install -y curl git openjdk-7-jre-headless apt-transport-https ca-
certificates \  
&& curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-
ci.org/public/org/jenkins-
ci/main/remoting/${JENKINS_REMOTING_VERSION}/remoting-${JENKINS_REMOTING_VERSION}.jar
\  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/slave.jar  
  
#  
# Install tools to control various Cloud platforms  
#  
# awscli  
RUN apt-get install -y python-pip \  
&& pip install awscli  
  
# gcloud  
ENV PATH=/usr/share/google-cloud-sdk/bin/:${PATH}  
ARG GCLOUD_VERSION=138.0.0  
RUN cd /usr/share/ \  
&& curl -sSLO
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz \  
&& tar xvf google-cloud-sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz \  
&& rm google-cloud-sdk-${GCLOUD_VERSION}-linux-x86_64.tar.gz \  
&& ./google-cloud-sdk/install.sh \  
&& yes | gcloud components install kubectl  
  
# docker  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo deb https://apt.dockerproject.org/repo debian-jessie main >
/etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get install -y docker-engine=$(apt-cache show docker-engine | grep -F
"Version: 1.7" | sort | tail -n1 | sed -r 's/Version: //')  

