FROM mysql:5.6  
MAINTAINER Vadim Slizov <z7zmey@gmail.com>  
  
ENV MYSQL_ROOT_PASSWORD pass  
ENV MYSQL_DATABASE gearman  
ENV MYSQL_USER gearman  
ENV MYSQL_PASSWORD gearman  
  
RUN apt-get update \  
&& apt-get -y install gearman-tools gearman-job-server mysql-client \  
&& apt-get clean  
  
COPY ./run.sh /run.sh  
  
CMD ["/run.sh"]  

