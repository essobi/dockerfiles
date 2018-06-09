#!/usr/bin/docker  
# stormsw/postgresql:v9.2  
FROM ubuntu:utopic  
MAINTAINER Alexander Varchenko <alexander.varchenko@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
# Add the PostgreSQL PGP key to verify their Debian packages.  
# It should be the same key as
https://www.postgresql.org/media/keys/ACCC4CF8.asc  
RUN apt-get install -y wget  
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc |
apt-key add -  
# Add PostgreSQL's repository. It contains the most recent stable release  
# of PostgreSQL, ``9.2``.  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ utopic-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
# Install ``python-software-properties``, ``software-properties-common`` and
PostgreSQL 9.2  
# There are some warnings (in red) that show up during the build. You can hide  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python-software-properties \  
software-properties-common \  
postgresql-9.2 \  
postgresql-client-9.2 \  
postgresql-contrib-9.2  
# Note: The official Debian and Ubuntu images automatically ``apt-get clean``  
# after each ``apt-get``  
ENV DEBIAN_FRONTEND newt  
# Run the rest of the commands as the ``postgres`` user created by the
``postgres-9.2`` package when it was ``apt-get installed``  
USER postgres  
  
# Create a PostgreSQL role named ``docker`` with ``docker`` as the password
and  
# then create a database `docker` owned by the ``docker`` role.  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'docker';" &&\  
createdb --template=template0 -E utf8 -O docker docker  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.2/main/pg_hba.conf  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.2/main/postgresql.conf  
# Expose the PostgreSQL port  
EXPOSE 5432  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]  
# Set the default command to run when starting the container  
CMD ["/usr/lib/postgresql/9.2/bin/postgres", "-D",
"/var/lib/postgresql/9.2/main", "-c",
"config_file=/etc/postgresql/9.2/main/postgresql.conf"]  

