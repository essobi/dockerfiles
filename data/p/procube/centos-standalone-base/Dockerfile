FROM centos:7  
MAINTAINER "Mitsuru Nakakawaji" <mitsuru@procube.jp>  
RUN yum -y update \  
&& yum -y install unzip wget sudo lsof telnet bind-utils tar tcpdump vim
sysstat strace less  
ENV HOME /root  
WORKDIR ${HOME}  
RUN echo "export TERM=xterm" >> .bash_profile  
ENV container docker  
STOPSIGNAL SIGRTMIN+3  
CMD [ "/sbin/init" ]  

