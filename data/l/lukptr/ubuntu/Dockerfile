FROM ubuntu:16.04  
MAINTAINER lukptr <lukptr@ridhosribumi.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
COPY ssh-keygen /usr/bin/  
RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& apt-get update \  
&& sed -i 's/101/0/g' /usr/sbin/policy-rc.d \  
&& apt-get install -y wget nano ca-certificates sudo cron python fontconfig \  
&& rm -rf /var/lib/apt/lists/* \  
&& chmod +x /usr/bin/ssh-keygen \  
&& echo "export TERM=dumb" >> ~/.bashrc  

