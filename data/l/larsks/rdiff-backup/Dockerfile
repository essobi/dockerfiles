FROM fedora  
MAINTAINER Lars Kellogg-Stedman <lars@oddbit.com>  
EXPOSE 22  
RUN yum -y install \  
openssh-server \  
passwd \  
rsync \  
rdiff-backup \  
; yum clean all  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/sshd", "-D"]  
  

