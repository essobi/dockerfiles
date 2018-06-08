# Shell Example:  
# docker run \  
# -p 137:137/udp -p 138:138/udp -p 139:139 -p 445:445 \  
# -v /var/docker_data/samba/share:/opt/samba/share \  
# -v /var/docker_data/samba/user:/opt/samba/user \  
# --name sambashare silvershell/samba  
FROM silvershell/ubuntu  
  
MAINTAINER silvershell  
  
ENV SMB_USER smbuser  
ENV SMB_PASSWORD smbpassword  
  
# ----------------  
RUN apt-get install -y samba supervisor  
  
# ----------------  
RUN mkdir -p /opt/samba/share  
RUN chmod 777 /opt/samba/share  
  
RUN mkdir -p /opt/samba/user  
RUN chmod 777 /opt/samba/user  
  
RUN useradd -s /bin/false "$SMB_USER"  
RUN (echo "$SMB_PASSWORD"; echo "$SMB_PASSWORD" ) | pdbedit -a -u "$SMB_USER"  
#For password change  
#RUN (echo "$SMB_PASSWORD"; echo "$SMB_PASSWORD" ) | smbpasswd -s -a
"$SMB_USER"  
# ----------------  
  
EXPOSE 137/udp 138/udp 139 445  
  
COPY smb.conf /etc/samba/smb.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
VOLUME /opt/samba/share /opt/samba/user  
  
CMD supervisord  
  

