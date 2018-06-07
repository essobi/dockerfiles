FROM phusion/baseimage:0.9.19  
  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl  
  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add \- \  
&& add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable" \  
&& apt-get update \  
&& apt-get install docker-ce -y  
  
#COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN mkdir /etc/service/docker  
ADD docker.sh /etc/service/docker/run  
  

