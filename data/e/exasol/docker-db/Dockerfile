FROM centos:6  
MAINTAINER EXASOL "service@exasol.com"  
RUN yum install openssh-server openssh-clients which sudo vim tar -y  
RUN echo "[ -z \"\$TERM\" -o \"\$TERM\" == \"dumb\" ] && export TERM=xterm"
>>/root/.bashrc  
RUN sed -i 's!.*UseDNS.*!UseDNS no!;s!.*UsePAM.*!UsePAM no!'
/etc/ssh/sshd_config  
  
ADD EXAClusterOS-6.0.rc2_LS-6.0.rc2-CentOS-6.8_x86_64.tar.gz /  
  
CMD /usr/opt/EXASuite-6/EXAClusterOS-6.0.rc2/libexec/exainit.py  

