# Centos Java and DSpace  
# VERSION 0.0.2  
FROM centos  
  
MAINTAINER Sam Ottenhoff ottenhoff@longsight.com  
  
RUN yum update -y  
RUN yum install -y java-1.7.0-openjdk postgresql-server postgresql poppler-
utils curl vim-enhanced perl  
RUN curl -o /tmp/tomcat.tar.gz
http://archive.apache.org/dist/tomcat/tomcat-7/v7.0.50/bin/apache-
tomcat-7.0.50.tar.gz  
RUN cd /var/  
RUN tar -xzvf /tmp/tomcat.tar.gz  
RUN mv apache-tomcat-7.0.50 /var/dspace-tomcat  
RUN chown -R daemon /var/dspace-tomcat  
  
RUN touch /etc/sysconfig/network  
RUN perl -pi -e 's/test x/#test x/g' /etc/init.d/postgresql  
RUN service postgresql initdb  
RUN perl -pi -e 's/ident/trust/g' /var/lib/pgsql/data/pg_hba.conf  
RUN service postgresql start  
#RUN createuser -Upostgres --createdb --no-createrole --no-password --no-
superuser dspace  
#RUN createdb -Udspace -E UNICODE -T template0 dspace  
CMD bash -l  
  
# run as the daemon user  
# USER daemon  
# expose Tomcat port  
EXPOSE 8080  

