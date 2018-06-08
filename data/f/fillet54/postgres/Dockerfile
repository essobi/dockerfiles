FROM centos:7  
ENV PGMAJOR 9.5  
ENV PGMAJORSLIM 95  
ENV PGPATCH 2  
ENV PGDATA /var/lib/pgsql/data  
ENV PGPORT 5432  
ENV PGBIN=/usr/pgsql-${PGMAJOR}/bin  
  
# Setup gosu for easier command execution  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-amd64.asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& rm -r /root/.gnupg/ \  
&& chmod +x /usr/local/bin/gosu  
  
# Install Postgresql  
# Disable base centos repos from pulling postgres  
# This can go away once we start maintaining our repos better  
RUN sed -e "s/\\[base\\]/\\[base\\]\nexclude=postgresql\\*/g" -e
"s/\\[updates\\]/\\[updates\\]\nexclude=postgresql\\*/g" -i
'/etc/yum.repos.d/CentOS-Base.repo'  
RUN curl -LO
https://download.postgresql.org/pub/repos/yum/${PGMAJOR}/redhat/rhel-7-x86_64/pgdg-
centos${PGMAJORSLIM}-${PGMAJOR}-${PGPATCH}.noarch.rpm \  
&& yum localinstall -y pgdg-
centos${PGMAJORSLIM}-${PGMAJOR}-${PGPATCH}.noarch.rpm \  
&& yum install -y postgresql${PGMAJORSLIM}.x86_64
postgresql${PGMAJORSLIM}-server.x86_64 \  
&& rm pgdg-centos${PGMAJORSLIM}-${PGMAJOR}-${PGPATCH}.noarch.rpm \  
&& yum clean all  
  
# Initialize the database  
RUN rm -rf ${PGDATA} \  
&& /usr/local/bin/gosu postgres mkdir ${PGDATA} \  
&& chmod go-rwx ${PGDATA} \  
&& sync \  
&& /usr/local/bin/gosu postgres ${PGBIN}/initdb --pgdata="${PGDATA}"
\--auth='ident' \  
&& /usr/local/bin/gosu postgres mkdir ${PGDATA}/pg_log \  
&& chmod go-rwx ${PGDATA}/pg_log  
  
ADD ./postgresql.conf ${PGDATA}/postgresql.conf  
RUN chown -v postgres.postgres ${PGDATA}/postgresql.conf  
RUN echo "host all all 0.0.0.0/0 md5" >> ${PGDATA}/pg_hba.conf  
  
VOLUME [${PGDATA}]  
EXPOSE ${PGPORT}  
CMD /usr/local/bin/gosu postgres /usr/pgsql-$PGMAJOR/bin/postgres -D $PGDATA
-p $PGPORT  
  

