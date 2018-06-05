## -*- docker-image-name: "mcreations/mariadb-backup" -*-  
FROM mcreations/openwrt-x64  
  
MAINTAINER Reza Rahimi <rahimi@m-creations.net>  
  
VOLUME /data/  
  
# must be specified when starting the container  
ENV DB_PASSWORD=""  
ENV DB_USER=""  
ENV DB_HOST=""  
ENV DB_NAME=""  
#bzip2 or gzip or zip  
ENV ZIP_CMD="bzip2"  
ENV DATE_FORMAT="%Y-%m-%d"  
ENV TIMESTAMP_FORMAT="%Y-%m-%d-%H_%M_%S-%Z"  
ENV DATADIR=/data  
  
ADD image/root/ /  
  
RUN opkg update && \  
opkg install mariadb-client mariadb-client-extra bzip2 && \  
rm /tmp/opkg-lists/*  
  
CMD ["/backup-mariadb.sh"]  
  

