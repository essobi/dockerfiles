FROM edwinhoksberg/base:latest  
LABEL maintainer="mail@edwinhoksberg.nl"  
  
# Install columnstore apt keys  
RUN wget -qO - https://downloads.mariadb.com/MariaDB/mariadb-
columnstore/MariaDB-ColumnStore.gpg.key | apt-key add - && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 28C12247  
  
# Install columnstore dependencies  
RUN apt-get update && \  
apt-get-safeinstall libboost-all-dev expect perl file sudo libdbi-perl
libncurses5 procps pwgen \  
libboost-all-dev libreadline-dev rsync net-tools libsnappy1v5 libreadline5
libaio1 libnuma1 syslog-ng  
  
# Copy scripts to image  
COPY rootfs /  
  
# Install columnstore itself  
RUN apt-get update && \  
apt-get-safeinstall mariadb-columnstore* mariadb-columnstore-api mariadb-
columnstore-tools \  
maxscale maxscale-cdc-connector #mariadb-columnstore-maxscale-cdc-adapters
mariadb-columnstore-kafka-adapters  
  
# Configure columnstore installation  
RUN /usr/local/mariadb/columnstore/bin/post-install && \  
/bin/echo -e "1\ncolumnstore-1\n1\n1\n" |
/usr/local/mariadb/columnstore/bin/postConfigure && \  
/init.sh  
  
EXPOSE 3306  
VOLUME /usr/local/mariadb/columnstore/etc  
VOLUME /usr/local/mariadb/columnstore/data1  
VOLUME /usr/local/mariadb/columnstore/local  
VOLUME /usr/local/mariadb/columnstore/mysql/db  
  
HEALTHCHECK \--interval=1m --timeout=10s --retries=3 \  
CMD /healthcheck.sh  
  
CMD ["/run.sh"]  

