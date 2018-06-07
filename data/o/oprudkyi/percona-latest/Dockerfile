# this image fixes official percona image
https://hub.docker.com/r/library/percona/  
# https://github.com/docker-library/percona/issues/40  
#  
# the /etc/mysql/conf.d/ has higher priority then /etc/mysql/percona-
server.conf.d/  
#  
  
FROM percona:latest  
  
ADD my.cnf /etc/mysql/my.cnf  
  
  

