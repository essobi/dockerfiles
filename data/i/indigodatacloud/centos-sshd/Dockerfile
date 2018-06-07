FROM centos:6  
LABEL eu.indigo-datacloud.type="linux"  
LABEL eu.indigo-datacloud.distribution="centos"  
LABEL eu.indigo-datacloud.version="6"  
LABEL eu.indigo-datacloud.architecture="amd64"  
  
RUN yum -y update; yum clean all  
RUN yum -y install epel-release; yum clean all  
  
#Pre-installed packages to speed IM contextualization  
RUN yum -y install \  
openssh \  
openssh-clients \  
openssh-server \  
python-distribute \  
wget \  
openssh-client \  
sshpass \  
ansible \  
&& yum clean all  
  
RUN easy_install pip  
  
RUN ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa  
  
RUN ssh-keygen -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa  
  
RUN echo "root:indig0!" | chpasswd  
  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
RUN yum install -y https://github.com/OpenNebula/addon-context-
linux/releases/download/v4.14.3/one-context_4.14.3.rpm  
  
RUN rm -f /etc/one-context.d/00-network; rm -f /etc/one-context.d/01-dns; rm
-f /etc/one-context.d/05-hostname; rm -f /etc/one-context.d/06-gen-env; rm -f
/etc/one-context.d/07-grow-rootfs  
  
COPY one-contextd /usr/sbin/one-contextd  
  
EXPOSE 22  
CMD /etc/init.d/vmcontext start; /usr/sbin/sshd -D  

