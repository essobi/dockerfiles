FROM ubuntu:16.04  
MAINTAINER Stephan Pieterse "https://github.com/stephanpieterse"  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:passME' | chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
WORKDIR /tmp  
  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install ca-certificates curl \  
&& curl -L -O
https://github.com/xmrig/xmrig/releases/download/v2.4.2/xmrig-2.4.2-gcc7-xenial-
amd64-no-api.tar.gz \  
&& tar -xvf xmrig-2.4.2-gcc7-xenial-amd64-no-api.tar.gz \  
&& rm xmrig-2.4.2-gcc7-xenial-amd64-no-api.tar.gz \  
&& mv xmrig-2.4.2/xmrig /usr/local/bin/xmrig \  
&& rm -r xmrig-2.4.2 \  
&& apt-get -y remove ca-certificates curl \  
&& apt-get clean autoclean \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

