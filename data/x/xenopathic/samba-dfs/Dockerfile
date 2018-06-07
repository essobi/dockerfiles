# DOCKER-VERSION 1.0.0  
#  
# Automated Samba test environment  
#  
# VERSION 0.0.1  
FROM silvershell/samba  
MAINTAINER Robin McCorkell "robin@mccorkell.me.uk"  
RUN userdel smbuser  
RUN pdbedit -x -u smbuser  
  
RUN mkdir -p /opt/samba/share /opt/samba/user /opt/samba/dfs  
RUN chmod 777 /opt/samba/share /opt/samba/user /opt/samba/dfs  
  
COPY smb.conf /etc/samba/smb.conf  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD supervisord  
  

