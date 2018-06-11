FROM centos:7  
ADD server01.sh /usr/local/bin/  
RUN chmod 755 /usr/local/bin/server01.sh  
RUN yum -y install passwd strace nc  
RUN passwd -d root && \  
cp /usr/bin/bash /usr/bin/rootshell && \  
chmod u+s /usr/bin/rootshell  
ENTRYPOINT ["server01.sh"]  

