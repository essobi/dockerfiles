FROM fedora:21  
RUN yum -y install libreoffice-headless libreoffice && yum clean all  
  
CMD /usr/bin/soffice --nologo --nofirststartwizard --headless --norestore
--invisible "--accept=socket,host=0.0.0.0,port=8100,tcpNoDelay=1;urp;"  
  

