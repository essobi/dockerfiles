FROM centos  
  
EXPOSE 8000 8080 3000 80 443  
  
  
ADD onlyoffice.repo /etc/yum.repos.d/onlyoffice.repo  
  
RUN set -xe;\  
rpm --import
"http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x8320CA65CB2DE8E5"; \  
yum install -y epel-release; \  
yum install -y onlyoffice-documentserver; \  
yum clean all  
  
  
ENV RABBIT_HOST=rabbit \  
RABBIT_PORT=5672 \  
RABBIT_USER=guest \  
RABBIT_PASSWORD=guest \  
POSTGRES_HOST=postgres \  
POSTGRES_PORT=5432 \  
POSTGRES_USER=onlyoffice \  
POSTGRES_PASSWORD=onlyoffice \  
POSTGRES_DB=onlyoffice \  
REDIS_HOST=redis \  
REDIS_PORT=6379 \  
DS_PORT=80  
  
#ENV DOCSERVICE_PORT=8000 \  
# SPELLCHECKER_PORT=8080 \  
# EXAMPLE_PORT=3000  
RUN yum install -y nmap-ncat && yum clean all  
ADD entrypoint.sh /entrypoint.sh  
ADD configure.sh /configure.sh  
  
ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  

