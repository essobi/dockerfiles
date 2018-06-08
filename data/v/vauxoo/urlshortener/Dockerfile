FROM python:3.4  
MAINTAINER Nhomar Hernandez <@ecreall.com>  
# Set the default command to run when starting the container  
CMD ["/usr/lib/"]  
RUN mkdir -p /app/var  
COPY . /app/  
RUN addgroup --quiet --gid "1000" "u1000" && \  
adduser \  
\--shell /bin/bash \  
\--disabled-password \  
\--force-badname \  
\--no-create-home \  
\--uid "1000" \  
\--gid "1000" \  
\--gecos '' \  
\--quiet \  
\--home "/app" \  
"u1000"  
WORKDIR /app  
RUN pip install -r requirements.txt  
RUN chown -R u1000:u1000 /app  
#  
# example Dockerfile for https://docs.docker.com/examples/postgresql_service/  
#  
# Add the PostgreSQL PGP key to verify their Debian packages.  
# It should be the same key as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
# Add PostgreSQL's repository. It contains the most recent stable release  
# of PostgreSQL, ``9.5``.  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
# Install ``python-software-properties``, ``software-properties-common`` and
PostgreSQL 9.3  
# There are some warnings (in red) that show up during the build. You can hide  
# them by prefixing each apt-get statement with DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common postgresql-9.5 postgresql-client-9.5 postgresql-contrib-9.5  
  
# Note: The official Debian and Ubuntu images automatically ``apt-get clean``  
# after each ``apt-get``  
# Run the rest of the commands as the ``postgres`` user created by the
``postgres-9.3`` package when it was ``apt-get installed``  
USER postgres  
  
# Create a PostgreSQL role named ``docker`` with ``docker`` as the password
and  
# then create a database `docker` owned by the ``docker`` role.  
# Note: here we use ``&&\\`` to run commands one after the other - the ``\\``  
# allows the RUN command to span multiple lines.  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER u1000 WITH CREATEDB;"  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host u1000 all 0.0.0.0/0 peer" >>
/etc/postgresql/9.5/main/pg_hba.conf  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.5/main/pg_hba.conf  
  
# And add ``listen_addresses`` to ``/etc/postgresql/9.5/main/postgresql.conf``  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf  
  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/app/var", "/etc/postgresql", "/var/log/postgresql",
"/var/lib/postgresql"]  
  
USER u1000  
  
EXPOSE 5432 5000  
CMD ["python", "main.py"]  

