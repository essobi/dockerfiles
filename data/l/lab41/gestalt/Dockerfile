FROM ubuntu:trusty  
MAINTAINER Charlie Lewis <charliel@lab41.org>  
  
ENV REFRESHED_AT 2016-09-06  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
RUN sed 's/us-east-1.ec2.archive.ubuntu.com/nova.clouds.archive.ubuntu.com/'
-i /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository ppa:ubuntu-toolchain-r/test  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update  
  
RUN apt-get install -y build-essential \  
git \  
libpq-dev \  
nodejs \  
npm \  
postgresql-9.4 \  
postgresql-client-9.4 \  
postgresql-contrib-9.4 \  
python-dev \  
python-psycopg2 \  
python-setuptools  
  
RUN easy_install pip  
RUN easy_install web.py  
RUN pip install --upgrade psycopg2  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN npm config set registry http://registry.npmjs.org/  
RUN npm install --global npm --save  
RUN npm install --global errno  
RUN npm install --global grunt karma grunt-karma --save-dev  
RUN npm install --global grunt-cli --save-dev  
RUN npm install --global grunt-contrib-imagemin --save-dev  
RUN npm install --global npm --save-dev  
RUN npm install --global yo --save-dev  
RUN npm install --global bower --save-dev  
  
ENV GESTALT_PULLED_AT 2016-09-12  
RUN git clone https://github.com/Lab41/gestalt.git  
  
WORKDIR /gestalt/prototypes/tablet  
RUN npm install angular --save  
RUN npm install pg --save  
RUN npm install express --save  
RUN npm install body-parser --save  
  
WORKDIR /gestalt/prototypes/desktop  
RUN npm install angular --save  
  
RUN sed 's/#\$ModLoad imudp/\$ModLoad imudp/' -i /etc/rsyslog.conf  
RUN sed 's/#\$UDPServerRun 514/\$UDPServerRun 514/' -i /etc/rsyslog.conf  
  
RUN touch /etc/rsyslog.d/50-default.conf  
RUN chown postgres:postgres /etc/rsyslog.d/50-default.conf  
RUN echo "postgres ALL=NOPASSWD: /etc/init.d/rsyslog start" >> /etc/sudoers  
  
USER postgres  
  
ADD *.sql /sql/  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" && \  
createdb -O docker users && \  
createdb gestalt && \  
psql -d gestalt -c "CREATE USER gestalt_user WITH SUPERUSER LOGIN PASSWORD
'umami';" && \  
psql -d gestalt -c 'CREATE EXTENSION "adminpack";'  
  
ENV PGPASSWORD umami  
ENV PGHOST 127.0.0.1  
ENV PGUSER gestalt_user  
ENV PGDATABASE gestalt  
RUN /etc/init.d/postgresql start &&\  
psql -f /sql/gestalt.sql  
  
USER root  
  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
  
EXPOSE 8000  
ENV DATABASE_URL gestalt,gestalt_user,127.0.0.1,umami,5432  
CMD (printf "*.*\t@$REMOTE_HOST" >> /etc/rsyslog.d/50-default.conf; \  
sudo /etc/init.d/rsyslog start; \  
logger started postgresql container $PARENT_HOST; \  
su - postgres -c "/usr/lib/postgresql/9.4/bin/postgres -c
config_file=/etc/postgresql/9.4/main/postgresql.conf >/tmp/logfile 2>&1") & \  
python /gestalt/prototypes/desktop/app.py  

