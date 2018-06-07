FROM sonatype/nexus3  
MAINTAINER Dave Woodward <dave@salte.io>  
  
USER root  
RUN yum update -y && yum install -y openssl  
RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum install -y libxml2 libxslt && yum clean all  
  
COPY *.xsl /tmp/.  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
EXPOSE 8443  
ENTRYPOINT ["/entrypoint.sh"]  

