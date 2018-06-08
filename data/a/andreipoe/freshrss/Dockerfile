FROM php:5.6-apache  
MAINTAINER Andrei Poenaru <andrei.poenaru@gmail.com>  
  
# Note: You shouldn't make all FreshRSS files public. See
https://github.com/FreshRSS/FreshRSS/tree/1.7.0#advices for more info.  
ENV FRSS_HOME="/srv/FreshRSS" \  
FRSS_LOG_DIR="/var/log/freshrss" \  
FRSS_SETUP_DIR="/data"  
ENV FRSS_DATA_DIR="${FRSS_HOME}/data"  
# Leave blank for the lastest stable verion  
ARG FRSS_VERSION  
  
RUN apt-get update \  
&& apt-get install -y libcurl4-openssl-dev libjpeg62-turbo-dev \  
libmcrypt-dev libpng12-dev libicu-dev libgmp-dev libsqlite3-dev \  
git \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& docker-php-ext-install curl mbstring gd intl mysql json zip gmp \  
pdo pdo_mysql pdo_sqlite \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -x && \  
mkdir -p "${FRSS_HOME}" && \  
cd "${FRSS_HOME}" && \  
git clone https://github.com/FreshRSS/FreshRSS.git . && \  
[ -n "${FRSS_VERSION}" ] && git checkout "${FRSS_VERSION}" || true && \  
chown -R :www-data . && \  
chmod -R g+r . && \  
chmod -R g+w data && \  
chmod -R g+w . && \  
cp -a data "${FRSS_SETUP_DIR}" && \  
rm -rf /var/www/html && \  
! echo "${FRSS_HOME}" | egrep -q '^/var/www/html' && ln -s "${FRSS_HOME}/p"
/var/www/html || echo "You should not set FRSS_HOME to /var/www/html. See
https://github.com/FreshRSS/FreshRSS/tree/1.7.0#advices for more info." >&2 &&
\  
apt-get autoremove -y git  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 80/tcp  
  
VOLUME ["${FRSS_DATA_DIR}", "${FRSS_LOG_DIR}"]  
WORKDIR ${FRSS_HOME}  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["app:start"]  
  

