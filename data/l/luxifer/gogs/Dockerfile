FROM debian:wheezy  
MAINTAINER luxifer666@gmail.com  
  
RUN apt-get -y update  
RUN apt-get -y install openssh-server unzip wget git supervisor  
  
RUN useradd -d /home/git -m -p "*" git  
USER git  
  
WORKDIR /home/git  
  
RUN mkdir /home/git/repositories  
RUN mkdir /home/git/.ssh  
  
RUN wget http://gogs.dn.qbox.me/gogs_v0.5.8_linux_amd64.zip  
RUN unzip gogs_v0.5.8_linux_amd64.zip  
  
RUN mkdir gogs/custom  
COPY conf/app.ini /home/git/gogs/custom/  
  
VOLUME ["/home/git/repositories", "/home/git/gogs/custom"]  
EXPOSE 2222 3000  
COPY conf/supervisord.conf /home/git/supervisord.conf  
COPY conf/sshd_config /home/git/.ssh/sshd_config  
  
RUN ssh-keygen -t rsa -q -N "" -f $HOME/.ssh/sshd_rsa  
RUN ssh-keygen -t rsa -q -N "" -f $HOME/.ssh/sshd_dsa  
CMD ["/usr/bin/supervisord", "-c", "/home/git/supervisord.conf"]  

