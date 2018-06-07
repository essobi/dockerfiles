FROM lazywei/cm_base:latest  
MAINTAINER Bert Chang "https://github.com/lazywei"  
# Workaround:
https://github.com/docker/docker/issues/783#issuecomment-56013588  
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/;
rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R
0700 /etc/ssl/private; chown -R postgres /etc/ssl/private  
  
# Run the rest of the commands as the ``postgres`` user created by the
``postgres-9.3`` package when it was ``apt-get installed``  
USER postgres  
  
# Create a PostgreSQL role named ``docker`` with ``docker`` as the password
and  
# then create a database `docker` owned by the ``docker`` role.  
# Note: here we use ``&&\\`` to run commands one after the other - the ``\\``  
# allows the RUN command to span multiple lines.  
RUN /etc/init.d/postgresql start &&\  
psql --command "CREATE USER codementor WITH SUPERUSER PASSWORD 'codementor';"
&&\  
createdb -O codementor codementor  
  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.3/main/pg_hba.conf  
  
# And add ``listen_addresses`` to ``/etc/postgresql/9.3/main/postgresql.conf``  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf  
  
# Expose the PostgreSQL port  
EXPOSE 5432  
# Add VOLUMEs to allow backup of config, logs and databases  
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql",
"/pg_data"]  
  
# Set the default command to run when starting the container  
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/pg_data", "-c",
"config_file=/etc/postgresql/9.3/main/postgresql.conf"]  

