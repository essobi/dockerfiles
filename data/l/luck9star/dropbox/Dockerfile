FROM centos  
ADD https://www.dropbox.com/download?plat=lnx.x86_64 /root/dropbox.tar.gz  
ADD https://www.dropbox.com/download?dl=packages/dropbox.py /bin/dropbox.py  
RUN yum update -y; yum install python -y && cd /root && tar xfvz
dropbox.tar.gz && rm dropbox.tar.gz && chmod +x /bin/dropbox.py  
CMD /root/.dropbox-dist/dropboxd  

