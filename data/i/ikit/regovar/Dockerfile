FROM python:3.6  
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ xenial-pgdg
main" >> /etc/apt/sources.list.d/pgdg.list'  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
RUN apt-get update -qy && apt-get -y --no-install-recommends install wget zip
gzip postgresql-9.6 # ca-certificates curl  
  
# # Setup gosu tool to manage user permissions with volume (between local and
container)  
# RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
# RUN curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture)" \  
# && curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-
architecture).asc" \  
# && gpg --verify /usr/local/bin/gosu.asc \  
# && rm /usr/local/bin/gosu.asc \  
# && chmod +x /usr/local/bin/gosu  
#  
# Regovar directories  
RUN mkdir -p /var/regovar/app  
RUN mkdir -p /var/regovar/_app  
RUN mkdir -p /var/regovar/cache  
RUN mkdir -p /var/regovar/downloads  
RUN mkdir -p /var/regovar/files  
RUN mkdir -p /var/regovar/pipelines  
RUN mkdir -p /var/regovar/jobs  
RUN mkdir -p /var/regovar/databases/hg19  
RUN mkdir -p /var/regovar/databases/hg38  
  
# Init Postgresql  
# RUN mkdir -p /var/regovar/sqldb  
# RUN chown postgres /var/regovar/sqldb  
RUN mv /etc/postgresql/9.6/main/ /etc/postgresql/9.6/old  
RUN su - postgres -c '/usr/lib/postgresql/9.6/bin/pg_ctl -D
/etc/postgresql/9.6/main/ initdb'  
  
# Copy regovar files  
COPY . /var/regovar/_app/  
RUN cp /var/regovar/_app/install/config.default
/var/regovar/_app/regovar/config.py  
RUN sed -i s/127\\.0\\.0\\.1/0\\.0\\.0\\.0/p
/var/regovar/_app/regovar/config.py  
RUN sed -i s/8500/80/p /var/regovar/_app/regovar/config.py  
RUN chmod a+rwx -R /var/regovar/_app/install  
RUN chmod a+x /var/regovar/_app/*.sh  
RUN chmod a+x /var/regovar/_app/regovar/*.py  
  
WORKDIR /var/regovar/_app  
RUN pip install -r /var/regovar/_app/requirements.txt  
RUN pip install -r /var/regovar/_app/requirements-dev.txt  
  
# Expose disks volumes and ports  
VOLUME ["/var/regovar/app", "/var/regovar/cache", "/var/regovar/downloads",
"/var/regovar/files", "/var/regovar/pipelines", "/var/regovar/jobs",
"/var/regovar/databases", "/etc/postgresql/9.6/main"]  
  
EXPOSE 80

