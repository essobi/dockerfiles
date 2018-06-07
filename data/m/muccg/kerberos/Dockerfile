FROM muccg/python-base:centos6-2.7  
MAINTAINER ccg <devops@ccg.murdoch.edu.au>  
  
ENV HOME /root  
  
RUN yum install -y \  
krb5-auth-dialog \  
krb5-libs \  
krb5-server \  
krb5-workstation \  
&& yum clean all  
  
RUN pip2.7 install supervisor  
  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
COPY supervisord/supervisord-krb5.conf /etc/supervisord.d/supervisord-
krb5.conf  
  
EXPOSE 9001 749 464 88  
ADD ./docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD "supervisord"  

