FROM ubuntu:16.04  
MAINTAINER DexterCai  
  
RUN apt-get update  
  
RUN apt-get install -y python2.7 python2.7-dev git git-flow screen  
RUN apt-get install -y build-essential libssl-dev libevent-dev libjpeg-dev
libxml2-dev libxslt-dev python-pip automake  
  
RUN git config --global alias.br branch  
RUN git config --global alias.ci commit  
RUN git config --global alias.co checkout  
RUN git config --global alias.st status  
RUN git config --global alias.lg "log --color --graph
--pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen (%cr) %C(bold
blue)<%an>%Creset' --abbrev-commit --"  
RUN git config --global user.name "Your Name"  
RUN git config --global user.email you@email.com  
RUN git config --global color.ui true  
  
RUN apt-get install build-essential  
  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:root' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN git clone https://github.com/dextercai/net-speeder.git ./jobs/net-speeder  
RUN sh ./jobs/net-speeder/build.sh  
  
RUN mv ./jobs/net_speeder /usr/local/bin/  
RUN chmod +x /usr/local/bin/net_speeder  
  
RUN git clone https://github.com/vbooter/DDoS-Scripts.git ./jobs/ddos  
RUN git clone https://github.com/shekyan/slowhttptest.git ./jobs/slowhttp  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

