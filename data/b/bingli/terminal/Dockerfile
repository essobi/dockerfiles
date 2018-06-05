FROM debian:7  
MAINTAINER Bing Li <enst.bupt@gmail.com>  
  
RUN apt-get update -y \  
&& apt-get install -y tmux git-core subversion curl bzip2 gzip vim wget
iptables net-tools procps openssh-server  
  
ENV HOME /root  
  
COPY vimrc ${HOME}/.vimrc  
COPY tmux.conf ${HOME}/.tmux.conf  
COPY ssh ${HOME}/.ssh  
COPY bashrc ${HOME}/.bashrc  
  
WORKDIR ${HOME}  
  
CMD /etc/init.d/ssh start; /bin/bash  

