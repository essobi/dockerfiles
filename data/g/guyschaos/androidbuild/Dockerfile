FROM tedwang/aosp-v5  
  
MAINTAINER guyschaos@gmail.com  
  
USER root  
  
RUN curl
http://archive.ubuntu.com/ubuntu/pool/universe/o/openjdk-8/openjdk-8-jre_8u45-b14-1_amd64.deb
> /tmp/jre8.deb \  
&& curl
http://archive.ubuntu.com/ubuntu/pool/universe/o/openjdk-8/openjdk-8-jre-
headless_8u45-b14-1_amd64.deb > /tmp/jre.deb \  
&& curl
http://archive.ubuntu.com/ubuntu/pool/universe/o/openjdk-8/openjdk-8-jdk_8u45-b14-1_amd64.deb
> /tmp/jdk.deb \  
&& dpkg -i /tmp/jre.deb && dpkg -i /tmp/jre8.deb && dpkg -i /tmp/jdk.deb \  
&& rm /tmp/jre.deb && rm /tmp/jre8.deb && rm /tmp/jdk.deb  
  
RUN apt-get update \  
&& apt-get install -y zip unzip lib32z1 lib32z1-dev bc ruby schedtool
liblz4-tool proxychains \  
&& apt-get clean  
  
RUN echo $'search china.HTC.COM.TW\n\  
nameserver 10.46.8.22\n\  
nameserver 10.46.8.23\n'\  
> /etc/resolv.conf  
  
USER android  
ENV USER=android  
  
RUN mkdir $HOME/code && mkdir $HOME/.ssh  
  
# RUN echo -e 'y\n'|ssh-keygen -q -t rsa -N "" -f ~/.ssh/id_rsa  
  

