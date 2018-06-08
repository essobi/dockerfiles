FROM centos:7  
MAINTAINER Scott Stevelinck <scott@fit-pay.com>  
  
RUN yum install -y ruby ruby-devel zlib-devel gcc patch make haproxy && yum
clean all  
  
RUN mkdir -p /synapse  
RUN gem install synapse -v 0.12.2 --no-document  
  
ADD haproxy.sh /haproxy.sh  
RUN chmod 755 /haproxy.sh  
  
ADD /synapse.conf.json /synapse-default.conf.json  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
ENTRYPOINT ["/run.sh"]  
CMD ["run"]  

