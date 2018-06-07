FROM buildpack-deps:sid-curl  
MAINTAINER Alexander De Leon <me@alexdeleon.name>  
  
# Install dependencies  
RUN apt-get update && apt-get -y install make postgresql php5 sudo supervisor  
  
# Set up locale  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
ENV LANG en_US.utf8  
  
  
# Install transmart-data  
ADD https://github.com/transmart/transmart-data/archive/v1.2.4.tar.gz
/opt/transmart-data.tar.gz  
RUN cd /opt; tar xzf transmart-data.tar.gz  
ADD vars /opt/transmart-data-1.2.4/vars  
RUN chown -R postgres:postgres /opt/transmart-data-1.2.4  
RUN chown -R postgres:postgres /var/lib/postgresql/9.4/main/  
  
# Init DB  
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/;
rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R
0700 /etc/ssl/private; chown -R postgres /etc/ssl/private &&
/etc/init.d/postgresql start && su postgres -c "cd /opt/transmart-data-1.2.4
&& . ./vars && skip_fix_tablespaces=1 make -j4"  
  
# Create supervisor config  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# work around for AUFS bug  
# as per https://github.com/docker/docker/issues/783#issuecomment-56013588  
RUN mkdir /etc/ssl/private-copy; mv /etc/ssl/private/* /etc/ssl/private-copy/;
rm -r /etc/ssl/private; mv /etc/ssl/private-copy /etc/ssl/private; chmod -R
0700 /etc/ssl/private; chown -R postgres /etc/ssl/private  
  
# replace existing listen_addresses entry by our own  
RUN perl -i -pe "s/.*listen_addresses.+/listen_addresses = '*'/"
/etc/postgresql/9.4/main/postgresql.conf  
# allow any connection to postgres  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.4/main/pg_hba.conf  
  
# Ports  
#postgresql  
EXPOSE 5432  
CMD ["/usr/bin/supervisord"]  

