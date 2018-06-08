FROM ubuntu:trusty  
MAINTAINER Daniel Yokomizo <daniel.yokomizo@gmail.com>  
  
RUN apt-get update \  
&& apt-get install --yes \  
nano \  
openjdk-7-jre \  
wget  
  
COPY squirrel-sql-3.7-standard.jar.sha512 /opt/squirrel-
sql-3.7-standard.jar.sha512  
COPY squirrel-sql-3.7-standard.xml /opt/squirrel-sql-3.7-standard.xml  
  
RUN wget --quiet --directory-prefix=/opt
http://ufpr.dl.sourceforge.net/project/squirrel-sql/1-stable/3.7.0/squirrel-
sql-3.7-standard.jar \  
&& sha512sum --check /opt/squirrel-sql-3.7-standard.jar.sha512 \  
&& java -jar /opt/squirrel-sql-3.7-standard.jar /opt/squirrel-
sql-3.7-standard.xml \  
&& rm /opt/squirrel-sql-3.7-standard.jar /opt/squirrel-
sql-3.7-standard.jar.sha512 /opt/squirrel-sql-3.7-standard.xml  
  
CMD ["/opt/squirrel-sql-3.7/squirrel-sql.sh"]  

