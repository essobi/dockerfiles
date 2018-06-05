FROM bitnami/minideb-extras:jessie-r68  
LABEL maintainer "Bitnami <containers@bitnami.com>"  
  
# Install required system packages and dependencies  
RUN install_packages libbz2-1.0 libc6 libcomerr2 libcurl3 libexpat1 libffi6
libfreetype6 libgcc1 libgcrypt20 libgmp10 libgnutls-deb0-28 libgpg-error0
libgssapi-krb5-2 libhogweed2 libicu52 libidn11 libjpeg62-turbo libk5crypto3
libkeyutils1 libkrb5-3 libkrb5support0 libldap-2.4-2 liblzma5 libmcrypt4
libncurses5 libnettle4 libp11-kit0 libpcre3 libpng12-0 libpq5 libreadline6
librtmp1 libsasl2-2 libsqlite3-0 libssh2-1 libssl1.0.0 libstdc++6 libsybdb5
libtasn1-6 libtidy-0.99-0 libtinfo5 libxml2 libxslt1.1 openssh-client zlib1g  
RUN bitnami-pkg unpack apache-2.4.33-4 --checksum
f26751a96abdc45db43c4b92eb9f792a4b630ad0edd5667aa73ccafa0aeb3810  
RUN bitnami-pkg unpack php-7.1.11-0 --checksum
2dbdbadb1a9020dfced88a368371781481c27d99956eec5d6b06ce27e796c16e  
RUN bitnami-pkg install mysql-client-10.1.25-0 --checksum
513ef36ab1efa5570332547c2027ae29886fe4bb56472de11ca083423a3fe366  
RUN bitnami-pkg install libphp-7.1.11-0 --checksum
9acea15fe83658d792dc6b272f406a155ec7ef2f91f61c2621a2d4213fc86f9d  
RUN bitnami-pkg install git-2.17.1-0 --checksum
948b00c283f89cac532ee3b2cd26b3efde12fe5425f25c6d836a96cebd35a8a7  
RUN bitnami-pkg unpack phabricator-2018.20.0-0 --checksum
c18b6ca33ff6ad390a3c85b742b653d5993ede2347805d93e1181d8db8ec525d  
  
COPY rootfs /  
ENV APACHE_HTTPS_PORT_NUMBER="443" \  
APACHE_HTTP_PORT_NUMBER="80" \  
BITNAMI_APP_NAME="phabricator" \  
BITNAMI_IMAGE_VERSION="2018.20.0-r6" \  
MARIADB_HOST="mariadb" \  
MARIADB_PASSWORD="" \  
MARIADB_PORT_NUMBER="3306" \  
MARIADB_USER="root" \  
PATH="/opt/bitnami/apache/bin:/opt/bitnami/php/bin:/opt/bitnami/mysql/bin:/opt/bitnami/git/bin:/opt/bitnami/arcanist/bin:/opt/bitnami/phabricator/bin:$PATH"
\  
PHABRICATOR_EMAIL="user@example.com" \  
PHABRICATOR_FIRSTNAME="FirstName" \  
PHABRICATOR_HOST="127.0.0.1" \  
PHABRICATOR_LASTNAME="LastName" \  
PHABRICATOR_PASSWORD="bitnami1" \  
PHABRICATOR_USERNAME="user" \  
SMTP_HOST="" \  
SMTP_PASSWORD="" \  
SMTP_PORT="" \  
SMTP_PROTOCOL="" \  
SMTP_USER=""  
EXPOSE 80 443  
ENTRYPOINT ["/app-entrypoint.sh"]  
CMD ["/run.sh"]  

