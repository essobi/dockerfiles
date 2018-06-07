FROM grossws/centos:7  
MAINTAINER Konstantin Gribov <grossws@gmail.com>  
  
EXPOSE 445  
VOLUME ["/data"]  
  
RUN yum install -y samba \  
&& yum clean all \  
&& echo "Adding rw user (uid=1000)" \  
&& useradd -s /bin/nologin -u 1000 -g users rw \  
&& echo -e "test\ntest" | smbpasswd -a rw \  
&& smbpasswd -e rw \  
&& echo "Adding ro user (uid=1001)" \  
&& useradd -s /bin/nologin -u 1001 -g users ro \  
&& echo -e "test\ntest" | smbpasswd -a ro \  
&& smbpasswd -e ro  
  
ADD entrypoint.sh smb.conf /  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["smbd"]  

