FROM ubuntu:14.04  
MAINTAINER VistaTeam_AppleBugs <2555085@qq.com>  
  
  
ENV TZ "Asia/Shanghai"  
ENV TERM xterm  
  
ADD resolv.conf /etc/resolv.conf  
  
#RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak  
#ADD apt-get_sources.list /etc/apt/sources.list  
RUN apt-get update  
  
RUN apt-get install openssh-server supervisor curl unzip daemon -y  
  
ADD supervisord.conf /etc/supervisord.conf  
  
RUN mkdir -p /etc/supervisor.conf.d && \  
mkdir -p /var/log/supervisor  
  
RUN echo 'root:docker' | chpasswd  
RUN mkdir /var/run/sshd  
RUN sed -i "s/PermitRootLogin without-password/PermitRootLogin yes/g"
/etc/ssh/sshd_config  
EXPOSE 22  
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  

