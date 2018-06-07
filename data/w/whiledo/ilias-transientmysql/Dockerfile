FROM whiledo/ilias-configured:latest  
MAINTAINER Kevin Krummenauer <kevin@whiledo.de>  
  
RUN apt-get update && apt-get install -y \  
mysql-server  
  
ENV containermysql_rootpw="my-secret-pw" \  
initmysql="yes" \  
remotemysql="no"  
WORKDIR /data  
ADD resources /data/resources/transientmysql  
  
RUN chown www-data:www-data /data/resources/transientmysql/entrypoint.sh \  
&& chmod 751 /data/resources/transientmysql/entrypoint.sh  
  
ENTRYPOINT ["/data/resources/transientmysql/entrypoint.sh"]  
  
EXPOSE 3306  

