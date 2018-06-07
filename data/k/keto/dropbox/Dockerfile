FROM centos:centos7  
  
MAINTAINER Mikael Keto  
  
# Install dropbox  
ADD https://www.dropbox.com/download?plat=lnx.x86_64 /dropbox.tar.gz  
ADD https://www.dropbox.com/download?dl=packages/dropbox.py
/usr/local/bin/dropbox.py  
RUN tar xfz /dropbox.tar.gz -C /opt/ && \  
mv /opt/.dropbox-dist /opt/dropbox && \  
rm /dropbox.tar.gz && \  
chmod +x /usr/local/bin/dropbox.py && \  
chown -R root:root /opt/dropbox  
  
EXPOSE 17500  
CMD /opt/dropbox/dropboxd  

