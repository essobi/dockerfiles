FROM centos:7  
MAINTAINER Gary Black "gary.black@causeway.com"  
RUN cd /tmp && curl -O
https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-
centos96-9.6-3.noarch.rpm && rpm -ivh pgdg-centos96-9.6-3.noarch.rpm && yum
install -y postgresql96-server.x86_64 postgresql96-contrib.x86_64
postgresql96-devel.x86_64 psmisc sudo  
ENV container docker  
  
RUN mkdir /data  
RUN chown postgres:postgres /data  
RUN chmod 700 /data  
RUN sudo -iu postgres touch /var/lib/pgsql/.pgsql_profile  
RUN sudo -iu postgres echo "export PGDATA=/data/9.6" >>
/var/lib/pgsql/.pgsql_profile  
RUN sudo -iu postgres echo "PATH=$PATH:/usr/pgsql-9.6/bin::" >>
/var/lib/pgsql/.pgsql_profile  
RUN sudo -iu postgres echo "export PATH" >> /var/lib/pgsql/.pgsql_profile  
RUN sudo -iu postgres echo "PS1='\h (Offline) $ '" >>
/var/lib/pgsql/.pgsql_profile  
RUN sudo -iu postgres printf "killall -0 --quiet postgres && export
PS1=\\`psql -c ' SELECT pg_is_in_recovery();' | grep --quiet f && echo '\h
(Primary) $ ' || echo '\h (Standby) $ '\\`" >> /var/lib/pgsql/.pgsql_profile  
RUN sudo -iu postgres mkdir /data/9.6  
  
ENV LANG en_GB.utf8  
ENV LANG en_GB.utf8  
ENV PGDATA /data/9.6  
RUN mkdir -p "$PGDATA" && chown -R postgres:postgres "$PGDATA" && chmod 777
"$PGDATA" # this 777 will be replaced by 700 at runtime (allows semi-arbitrary
"--user" values)  
  
EXPOSE 5432  

