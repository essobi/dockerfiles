FROM weepee/centos7  
  
RUN yum install -y {e4fs,xfs}progs man wget perl vim sudo mailx yum-utils && \  
yum install -y htop ncurses-term bind-utils zsh && \  
yum clean all  
RUN yum install -y git && \  
yum clean all  

