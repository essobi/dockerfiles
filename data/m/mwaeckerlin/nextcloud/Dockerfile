FROM mwaeckerlin/ubuntu-base  
MAINTAINER mwaeckerlin  
  
EXPOSE 80  
ENV UPLOAD_MAX_FILESIZE "8G"  
ENV MAX_INPUT_TIME "3600"  
ENV WEBROOT ""  
ENV ADMIN_USER ""  
ENV ADMIN_PWD ""  
ENV URL ""  
ENV DEBUG "0"  
# compile time variables  
ENV INSTBASE "/var/www"  
ENV INSTDIR "${INSTBASE}/nextcloud"  
ENV DATADIR "${INSTDIR}/data"  
ENV CONFDIR "${INSTDIR}/config"  
ENV APPSDIR "${INSTDIR}/apps"  
ENV SOURCE_FILE="latest.tar.bz2"  
# test if 13.0.0 is fixed: https://github.com/nextcloud/server/issues/8240  
#ENV SOURCE_FILE="nextcloud-12.0.5.tar.bz2"  
ENV SOURCE="https://download.nextcloud.com/server/releases/${SOURCE_FILE}"  
WORKDIR /tmp  
  
ADD nextcloud.asc /nextcloud.asc  
ADD start.sh /start.sh  
ADD nextcloud.conf /nextcloud.conf  
  
RUN apt-get update && apt-get install -y gnupg bzip2 pwgen sudo apache2
libapache2-mod-php7.0 php7.0-gd php7.0-json php7.0-mysql php7.0-curl
php7.0-mbstring php7.0-intl php7.0-mcrypt php-imagick php7.0-xml php7.0-zip
php-apcu php-ldap rsync php-imagick libmagickcore-extra wget cron  
RUN mkdir -p "${INSTDIR}"  
RUN wget -qO${SOURCE_FILE} ${SOURCE}  
RUN wget -qO${SOURCE_FILE}.asc ${SOURCE}.asc  
RUN gpg --import /nextcloud.asc  
RUN gpg --verify ${SOURCE_FILE}.asc ${SOURCE_FILE}  
  
WORKDIR "${INSTBASE}"  
RUN tar xf /tmp/${SOURCE_FILE}  
RUN rm /tmp/${SOURCE_FILE} /tmp/${SOURCE_FILE}.asc /nextcloud.asc  
WORKDIR "${INSTDIR}"  
RUN chmod +x occ  
RUN mkdir data  
RUN chown -R www-data config apps data  
RUN mv $APPSDIR ${APPSDIR}.original  
RUN mkdir $APPSDIR  
RUN chown www-data.www-data $APPSDIR  
RUN ln -sf /proc/1/fd/1 /var/log/apache2/access.log  
RUN ln -sf /proc/1/fd/2 /var/log/apache2/error.log  
RUN ln -sf /proc/1/fd/1 /var/log/nextcloud.log  
  
VOLUME $DATADIR  
VOLUME $CONFDIR  
VOLUME $APPSDIR  
WORKDIR $INSTDIR  

