FROM eeacms/postgres:9.5  
MAINTAINER michimau <mauro.michielon@eea.europa.eu>  
  
RUN apt-get -y update && apt-get -y install \  
vim \  
curl  
  
COPY sh/apply_set_roles.sh /  
COPY sh/create_roles_file.sh /  
  
COPY sh/initialize_db.sh /  
COPY sh/entrypoint.sh /  
COPY sh/create_ssl_files.sh /  
  
COPY conf/ssl.conf /postgresql.conf.d/  
COPY conf/pg_hba.conf /  
  
COPY sql/groups.sql /  
COPY sql/groups_permissions.sql /  
COPY sql/create_role_if_not_exists.sql /  
  
RUN curl -sS
http://www.sparxsystems.com/downloads/corp/scripts/EASchema_1220_PostgreSQL.sql
> /EASchema_1220_PostgreSQL.sql  
RUN curl -sS
http://www.sparxsystems.com/downloads/corp/scripts/EABase_1220_Postgres.sql >>
/EASchema_1220_PostgreSQL.sql  
  
RUN echo "sh /initialize_db.sh" >> /docker-entrypoint-initdb.d/setup-schema.sh  
  
RUN sed -i -e 's/exec gosu postgres "$@"/sh \/create_roles_file.sh \&\nexec
gosu postgres "$@"/g' /docker-entrypoint.sh  
RUN sed -i -e 's/exec gosu postgres "$@"/sh \/apply_set_roles.sh \&\nexec gosu
postgres "$@"/g' /docker-entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["postgres"]  

