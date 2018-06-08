FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
man-db \  
openssh-server \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/run/sshd  
  
ADD ./docker-run.sh /usr/local/bin/docker-run  
  
EXPOSE 22  
CMD ["/usr/local/bin/docker-run"]  

