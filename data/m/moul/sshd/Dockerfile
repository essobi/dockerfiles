FROM ubuntu:latest  
MAINTAINER Manfred Touron m@42.am  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg-divert --local \--rename --add /sbin/initctl && \  
ln -s /bin/true /sbin/initctl || true  
  
RUN apt-get -qq -y install openssh-server && \  
apt-get clean  
  
RUN mkdir -p /var/run/sshd && \  
echo "root:root" | chpasswd  
  
CMD ["/usr/sbin/sshd", "-D"]  
  
EXPOSE 22  

