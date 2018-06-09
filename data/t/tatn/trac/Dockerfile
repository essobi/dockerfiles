FROM httpd:2.4  
MAINTAINER Noguchi Tatsuya <noguchi.ta@gmail.com>  
  
RUN apt-get -y update  
RUN apt-get install -y libapache2-mod-wsgi  
RUN apt-get install -y libapache2-mod-python  
RUN apt-get install -y python-setuptools  
RUN apt-get install -y python-genshi  
RUN apt-get install -y git-core  
  
RUN apt-get install -y trac  
RUN apt-get install -y python-mysqldb  
RUN apt-get install -y python-psycopg2  
  
RUN apt-get install -y trac-accountmanager  
RUN apt-get install -y trac-announcer  
RUN apt-get install -y trac-codecomments  
RUN apt-get install -y trac-customfieldadmin  
RUN apt-get install -y trac-graphviz  
RUN apt-get install -y trac-httpauth  
RUN apt-get install -y trac-includemacro  
RUN apt-get install -y trac-ja-resource  
RUN apt-get install -y trac-mastertickets  
RUN apt-get install -y trac-navadd  
RUN apt-get install -y trac-subcomponents  
RUN apt-get install -y trac-subtickets  
RUN apt-get install -y trac-tags  
RUN apt-get install -y trac-xmlrpc  
RUN apt-get install -y vim  
  
EXPOSE 80 443  
RUN mkdir /var/tracwork  
COPY trac.wsgi /var/tracwork/trac.wsgi  
COPY httpd.conf /var/tracwork/httpd.conf  
COPY set-trac-env.sh /var/tracwork/set-trac-env.sh  
COPY docker-entrypoint.sh /var/tracwork/entrypoint.sh  
  
VOLUME /var/trac  
  
ENTRYPOINT ["/var/tracwork/entrypoint.sh"]  
CMD ["httpd-foreground"]  
  

