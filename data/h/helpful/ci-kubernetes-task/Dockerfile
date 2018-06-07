FROM ubuntu:latest  
MAINTAINER Helpful version: 1.0  
RUN apt-get update -y \  
&& apt-get install -y apt-transport-https ca-certificates  
  
RUN echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | tee
/etc/apt/sources.list.d/docker.list  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
  
RUN apt-get update -y \  
&& apt-get install -y python docker-engine git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-133.0.0-linux-x86_64.tar.gz /tmp/gcloud.tar.gz  
RUN cd / && tar -zxvf /tmp/gcloud.tar.gz  
  
RUN (cd /google-cloud-sdk \  
&& ./install.sh --quiet) \  
&& /google-cloud-sdk/bin/gcloud components install kubectl --quiet  
  
# ADD gcloud sdk to PATH  
RUN echo "source '/google-cloud-sdk/path.bash.inc'" >> /root/.bash_profile  
  
## Jfrog does not work on Alpine Linux. See:
https://www.jfrog.com/jira/browse/RTFACT-9985  
ADD https://api.bintray.com/content/jfrog/jfrog-cli-go/\$latest/jfrog-cli-
linux-amd64/jfrog?bt_package=jfrog-cli-linux-amd64 /usr/local/bin/jfrog  
RUN chmod a+x /usr/local/bin/jfrog  

