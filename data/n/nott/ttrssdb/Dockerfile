FROM nott/ttrss  
MAINTAINER Stas Rudakou "stas@garage22.net"  
RUN yum -y install postgresql-server sudo  
  
RUN sed -i -e '2,2ialias system=echo' -e '2,2ifunction systemctl() { echo
"Environment=PGPORT=5432 PGDATA=/var/lib/pgsql/data"; }' /usr/bin/postgresql-
setup && \  
(tail -F /var/lib/pgsql/initdb.log & tailpid=$!; \  
export $(locale 2>>/dev/null|tr -d '\\\"') ; \  
/usr/bin/postgresql-setup initdb && \  
kill $tailpid )  
  
RUN sudo --user postgres pg_ctl -w start -D /var/lib/pgsql/data && \  
echo "CREATE USER ttrss WITH PASSWORD 'ttrss';" | sudo --user postgres psql &&
\  
echo "CREATE DATABASE ttrss;" | sudo --user postgres psql && \  
echo "GRANT ALL PRIVILEGES ON DATABASE ttrss TO ttrss;" | sudo --user postgres
psql && \  
useradd ttrss && \  
sed "s/--[^;]*;//g" /opt/tt-rss/schema/ttrss_schema_pgsql.sql | tr "\n" " " |
tr ";" ";\n" | sudo --user ttrss psql && \  
userdel -r ttrss && \  
sudo --user postgres pg_ctl -w stop -D /var/lib/pgsql/data && \  
echo "host all all 0.0.0.0/0 md5" >> /var/lib/pgsql/data/pg_hba.conf && \  
echo "listen_addresses='*'" >> /var/lib/pgsql/data/postgresql.conf  
  
VOLUME = ["/var/lib/pgsql/data"]  
  
EXPOSE 5432  
USER postgres  
  
CMD /usr/bin/postgres -D /var/lib/pgsql/data/

