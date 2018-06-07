FROM percona/percona-server:5.7  
MAINTAINER Alexander Marinov <alexander.marinov@web-lab.ltd>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Get back to root after base image forced the mysql user  
USER 0  
RUN sed -i 's/3306/3307/g' /etc/mysql/my.cnf  
  
# Re-apply the user enforcement  
USER 1001  
EXPOSE 3307  

