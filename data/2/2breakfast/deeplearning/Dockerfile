FROM 2breakfast/deeplearning:py-caffe0.15-cuda8.0-cudnn5-devel-ubuntu14.04  
MAINTAINER Weitao Zhou <wtzhou@dataman-inc.com>  
  
RUN rm -rf /var/lib/apt/lists/* && apt-get update && apt-get install -qq ldap-
utils ldap-auth-client libnss-ldap libpam-ldap autofs  
  
ENV LDAP_ADDR ldap://10.1.0.201/  
ENV NFS_ADDR 10.1.0.180  
ADD etc/ /etc/  
ADD entrypoint.sh /usr/local/sbin/entrypoint.sh  
  
RUN chmod a+x /usr/local/sbin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]  
  
CMD ["/usr/sbin/sshd", "-D"]  

