FROM bitnami/minideb-extras:jessie-r68  
LABEL maintainer "Bitnami <containers@bitnami.com>"  
  
# Install required system packages and dependencies  
RUN install_packages cron libbz2-1.0 libc6 libcomerr2 libcurl3 libexpat1
libffi6 libfreetype6 libgcc1 libgcrypt20 libgmp10 libgnutls-deb0-28 libgpg-
error0 libgssapi-krb5-2 libhogweed2 libicu52 libidn11 libjpeg62-turbo
libk5crypto3 libkeyutils1 libkrb5-3 libkrb5support0 libldap-2.4-2 liblzma5
libmcrypt4 libncurses5 libnettle4 libp11-kit0 libpcre3 libpng12-0 libpq5
libreadline6 librtmp1 libsasl2-2 libsqlite3-0 libssh2-1 libssl1.0.0 libstdc++6
libsybdb5 libtasn1-6 libtidy-0.99-0 libtinfo5 libxml2 libxslt1.1 zlib1g  
RUN bitnami-pkg unpack apache-2.4.33-4 --checksum
f26751a96abdc45db43c4b92eb9f792a4b630ad0edd5667aa73ccafa0aeb3810  
RUN bitnami-pkg unpack php-7.1.18-1 --checksum
56f43b9ae65d24e2602ad4c1f1af6392be92a281684c80d62ba81c195d372c97  
RUN bitnami-pkg unpack mysql-client-10.1.33-0 --checksum
1b1608f1c1f4e21f05037225e095c49035ad8bfdb8b580abbb904c9f2448a5c6  
RUN bitnami-pkg install libphp-7.1.18-2 --checksum
d6b0e8686332b5af34c988412a2a1b18ba2fd6dda8781b9dc7c6ea3b243aba89  
RUN bitnami-pkg unpack moodle-3.5.0-3 --checksum
a26bdc232d3ead20d51c91cb17903c64700684ae060bdfe0e8820e64717c658e  
RUN sed -i -e '/pam_loginuid.so/ s/^#*/#/' /etc/pam.d/cron  
  
COPY rootfs /  
ENV ALLOW_EMPTY_PASSWORD="no" \  
APACHE_HTTPS_PORT_NUMBER="443" \  
APACHE_HTTP_PORT_NUMBER="80" \  
BITNAMI_APP_NAME="moodle" \  
BITNAMI_IMAGE_VERSION="3.5.0-r10" \  
MARIADB_HOST="mariadb" \  
MARIADB_PORT_NUMBER="3306" \  
MARIADB_ROOT_PASSWORD="" \  
MARIADB_ROOT_USER="root" \  
MOODLE_DATABASE_NAME="bitnami_moodle" \  
MOODLE_DATABASE_PASSWORD="" \  
MOODLE_DATABASE_USER="bn_moodle" \  
MOODLE_EMAIL="user@example.com" \  
MOODLE_LANGUAGE="en" \  
MOODLE_PASSWORD="bitnami" \  
MOODLE_SITENAME="New Site" \  
MOODLE_USERNAME="user" \  
MYSQL_CLIENT_CREATE_DATABASE_NAME="" \  
MYSQL_CLIENT_CREATE_DATABASE_PASSWORD="" \  
MYSQL_CLIENT_CREATE_DATABASE_PRIVILEGES="ALL" \  
MYSQL_CLIENT_CREATE_DATABASE_USER="" \  
PATH="/opt/bitnami/apache/bin:/opt/bitnami/php/bin:/opt/bitnami/mysql/bin:$PATH"
\  
SMTP_HOST="" \  
SMTP_PASSWORD="" \  
SMTP_PORT="" \  
SMTP_PROTOCOL="" \  
SMTP_USER=""  
EXPOSE 80 443  
ENTRYPOINT ["/app-entrypoint.sh"]  
CMD ["/run.sh"]  

