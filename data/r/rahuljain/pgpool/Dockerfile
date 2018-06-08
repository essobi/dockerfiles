###############################################################################################  
# Dockerfile used to create pgpool-II container image.  
#  
# Run: READ.md  
###############################################################################################  
  
FROM rahuljain/base:1.0.0  
  
LABEL maintainer="rahuljain"  
  
ENV VERSION 3.7.0  
ENV PGPOOL_VERSION 3.7.0  
ENV POSTGRESQL_VERSION 9.5.12  
ENV LANG en_US.utf8  
  
  
# install pgpool rsync  
RUN apk --update --no-cache add py-psycopg2 pgpool postgresql-
client=${POSTGRESQL_VERSION}-r0 --update-cache --repository
http://dl-3.alpinelinux.org/alpine/v3.4/main --allow-untrusted && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir /etc/pgpool-II /var/run/pgpool && \  
chown postgres /etc/pgpool-II /var/run/pgpool  
  
EXPOSE 5432  
  
COPY templates /etc/pgpool-II/templates  
  
COPY run.py /run.py  
RUN chmod +x /run.py  
  
CMD ["/run.py"]  

