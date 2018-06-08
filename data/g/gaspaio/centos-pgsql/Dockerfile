# Inspired by: Better config cf. https://github.com/zaiste/docker-postgresql  
FROM gaspaio/base-centos:latest  
MAINTAINER Rodolfo Ripado <ggaspaio@gmail.com>  
  
# Install PG 9.3  
RUN rpm -Uvh http://yum.postgresql.org/9.3/redhat/rhel-6-x86_64/pgdg-
centos93-9.3-1.noarch.rpm  
RUN yum install postgresql93-server postgresql-contrib -y  
  
ADD run /bin/run  
RUN chmod +x /bin/run  
  
# expose PG port  
EXPOSE 5432  
# Start server  
CMD ["/bin/run"]  
  

