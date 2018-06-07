FROM endika/base  
  
MAINTAINER me@endikaiglesias.com  
  
ENV ODOO_PASS 'welcome'  
RUN aptitude install -y postgresql-9.3  
RUN /etc/init.d/postgresql start  
  
USER postgres  
RUN /etc/init.d/postgresql start && \  
psql --command "CREATE USER odoo WITH PASSWORD '$ODOO_PASS';ALTER USER odoo
WITH SUPERUSER;"  
RUN rm /var/run/postgresql/.s.PGSQL.5432.lock  
  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
CMD ["postgres"]  
EXPOSE 5432  

