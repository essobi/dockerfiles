FROM relateiq/oracle-java8  
MAINTAINER Igor Hjelmstrom Vinhas Ribeiro <igorhvr@iasylum.net>  
# Erase apt-get caches, then run update operation.  
ENV TERM xterm  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "2015-02-26" > /last_apt-get_update  
RUN cd /var/lib/apt ; rm -rf *  
RUN apt-get -y update --fix-missing  
RUN apt-get install -y git  
RUN cd / ; mkdir base ; cd base ; git clone
https://github.com/igorhvr/bedlam.git ; chmod -R 755 /base  
RUN apt-get install -y zsh  
RUN curl -L https://github.com/igorhvr/oh-my-zsh/raw/master/tools/install.sh |
/bin/bash  
RUN apt-get -y install screen  
ADD .screenrc /root/.screenrc  
RUN apt-get -y install mosh  
RUN apt-get -y install htop  
RUN apt-get -y install emacs  
RUN apt-get -y install telnet  
RUN apt-get -y install w3m  
RUN apt-get -y install openssh-server  
RUN apt-get -y install rsync  
RUN apt-get -y install zip  
RUN apt-get -y install unzip  
RUN apt-get -y install psmisc  
RUN apt-get -y install less  
RUN apt-get -y install ntpdate  
  
RUN echo 'root:root' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ADD id_rsa.pub /root/.ssh/authorized_keys  
RUN chmod -R 700 /root/.ssh/  
  
RUN echo '#!/bin/sh\n/etc/init.d/ssh start\n/base/bedlam/schejure/sj\nsleep
infinity' > /start-network-services ; chmod 755 /start-network-services  
RUN echo '#!/bin/sh\n/base/bedlam/sisc/sisc-1.16.6/sisc $*' > /sisc ; chmod
755 /sisc  
ADD data/ /data  
  
RUN echo "2015-02-26_02h13mUTC" > /last_git_pull  
RUN cd /base/bedlam ; git reset --hard HEAD ; git pull  
  
ENV LANG C.UTF-8  
CMD ["/bin/zsh"]  
  
# ssh  
EXPOSE 22  
# Sisc Repl  
EXPOSE 3000  
# Beanshell httpd service  
EXPOSE 3001  
# Beanshell raw  
EXPOSE 3002  
# Clojure nrepl  
EXPOSE 6000  
# Clojure tty transport  
EXPOSE 6001  

