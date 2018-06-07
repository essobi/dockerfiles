FROM ubuntu:14.04  
MAINTAINER Elmer Salazar  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update && \  
apt-get install -qq -y \  
python-pip \  
python-dev \  
python-lxml \  
libldap2-dev \  
unoconv \  
libpq-dev \  
git \  
mercurial \  
npm \  
fish \  
freetds-dev libsasl2-dev \  
postgresql-client \  
build-essential \  
python-software-properties \  
software-properties-common \  
libjpeg-dev \  
libfreetype6 \  
libfreetype6-dev \  
zlib1g-dev \  
postgresql-9.3 postgresql-client-9.3 \  
postgresql-contrib-9.3 \  
default-jre-headless && \  
apt-get clean && \  
rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
USER postgres  
RUN /etc/init.d/postgresql start \  
&& psql --command "CREATE USER pguser WITH SUPERUSER PASSWORD 'pguser';" \  
&& createdb -O pguser pgdb  
  
USER root  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
RUN mkdir -p /var/run/postgresql && chown -R postgres /var/run/postgresql  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
USER postgres  
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D",
"/var/lib/postgresql/9.3/main", "-c",
"config_file=/etc/postgresql/9.3/main/postgresql.conf"]  
  
USER root  
  
RUN mkdir -p /var/lib/trytond  
RUN mkdir -p /app  
  
WORKDIR /app/  
  
RUN hg clone https://bitbucket.org/huntergps/tryton-tasks tasks  
RUN pip install -r tasks/requirements.txt  
  
ADD bootstrap.py /app/tasks/bootstrap.py  
ADD config /app/config  
  
RUN invoke bs  
  
RUN cd public_data/sao && \  
npm install grunt bower && \  
npm install && \  
nodejs node_modules/.bin/grunt --force && \  
nodejs node_modules/.bin/bower --allow-root \  
\--config.interactive=false \--production \  
\--force-latest install  
  
ADD trytond.conf /etc/trytond.conf  
ADD trytond-logconf.conf /etc/trytond-logconf.conf  
RUN find /app -name .hg -type d -exec echo rm -r {} \;  
VOLUME /var/lib/trytond  
  
EXPOSE 8000 8002 5432  
ADD run.sh /app/  
  
CMD ["/app/run.sh"]  
  
CMD ["chsh -s /usr/bin/fish"]  

