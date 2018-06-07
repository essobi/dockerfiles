FROM mysql:5.5  
MAINTAINER nils.kuhn@iteratec.de  
  
# add mysql custom config for rearview  
ADD mysql/conf.d /etc/mysql/conf.d  
VOLUME /etc/mysql/conf.d  
  
# publish mysql data-dir volume  
VOLUME /var/lib/mysql

