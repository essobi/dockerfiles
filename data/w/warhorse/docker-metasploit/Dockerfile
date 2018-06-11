FROM kalilinux/kali-linux-docker  
MAINTAINER Ralph May <ralph@thedarkcloud.net>  
  
RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >>
/etc/apt/sources.list  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get clean  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
ruby \  
metasploit-framework \  
openssh-server  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /var/run/sshd  
RUN mkdir /root/.ssh  
COPY ./docker-entrypoint.sh /root/  
RUN chmod +x /root/docker-entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["/root/docker-entrypoint.sh"]

