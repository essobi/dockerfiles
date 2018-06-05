FROM debian:latest  
MAINTAINER Sohaib AFIFI  
  
  
# RUN echo 'Acquire::http::Proxy "http://cache-etu.univ-artois.fr:3128";'
>/etc/apt/apt.conf.d/00-proxy  
# ENV all_proxy cache-adm.univ-artois.fr:8080  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install wget supervisor locales
subversion curl cracklib-runtime apache2 ssl-cert insserv postgresql-9.6
postgresql-client-9.6 graphviz python-docutils python-jaxml python-psycopg2
python-pyrss2gen python-imaging python-reportlab python-cracklib python-
beautifulsoup python-egenix-mxtools python-egenix-mxdatetime python-six
python-gdbm python-tk python-pydot  
RUN cd /opt && \  
wget http://www-l2ti.univ-paris13.fr/~viennet/ScoDoc/builds/scodoc-1632.tgz
&&\  
tar xfz scodoc-1632.tgz && \  
cd /opt/scodoc/Products/ScoDoc/ &&\  
svn up && \  
cd /opt/scodoc/Products/ScoDoc/config && \  
service postgresql start &&\  
./create_user_db.sh || true && \  
chsh www-data -s /bin/bash && \  
./create_user_db.sh  
  
COPY ./root /  
RUN /usr/sbin/locale-gen --keep-existing  
RUN mkdir -p /etc/apache2/scodoc-ssl &&\  
/usr/sbin/make-ssl-cert /usr/share/ssl-cert/ssleay.cnf /etc/apache2/scodoc-
ssl/apache.pem  
  
RUN a2enmod ssl proxy proxy_http rewrite  
RUN a2ensite scodoc-site-ssl  
  
CMD ["/usr/bin/supervisord"]  
EXPOSE 443 80 5432 8080  

