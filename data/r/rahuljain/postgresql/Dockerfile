###############################################################################################  
# Dockerfile used to create postgresql container image.  
#  
# See: README.md  
###############################################################################################  
  
FROM rahuljain/base:1.0.0  
  
LABEL maintainer="rahuljain"  
  
ENV VERSION 9.5.12  
ENV POSTGRESQL_VERSION=9.5.12  
  
# install postgresql and pgpool libraries from package manager and clean apk
cache  
RUN apk add --no-cache --update py-psycopg2 pgpool
postgresql=${POSTGRESQL_VERSION}-r0 postgresql-client=${POSTGRESQL_VERSION}-r0
postgresql-contrib=${POSTGRESQL_VERSION}-r0 \  
\--update-cache --repository http://dl-3.alpinelinux.org/alpine/v3.4/main
--allow-untrusted && \  
pip install flask && \  
mkdir -p /opt/pgsql/data && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 5432 5000  
  
COPY templates /opt/pgsql_templates  
  
COPY run.py /run.py  
RUN chmod +x /run.py  
  
CMD ["/run.py"]  

