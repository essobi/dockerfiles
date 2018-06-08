FROM centos:7  
RUN yum -y install PyYAML rsyslog cronie  
  
COPY entrypoint.sh /  
#COPY entrypoint.py /  
ADD https://raw.githubusercontent.com/masakazuwatanabe/docker-
entrypoint/master/entrypoint.py /  
COPY entrypoint.yml /  
RUN chmod +x /entrypoint.sh /entrypoint.py  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD []  

