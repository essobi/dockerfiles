FROM owncloud/base:latest AS build  
MAINTAINER neffets <software@neffets.de>  
  
RUN curl -sLo -
https://download.owncloud.org/community/owncloud-10.0.3.tar.bz2 | tar xfj - -C
/var/www/  
#ADD owncloud-10.0.3.tar.bz2 /var/www/  
COPY ./entrypoint-70-enable-userexternal.sh /etc/entrypoint.d/.  
COPY source/ /  
  
RUN curl -sLo user_ldap.tar.gz
https://github.com/owncloud/user_ldap/releases/download/0.9.1/user_ldap.tar.gz
&& echo "f9e0aa49f8dde4f1eccb69252e09f8e65f11e1fe5c222f22cbafd3ffede53331
user_ldap.tar.gz" | sha256sum -c - && mkdir -p
/var/www/owncloud/apps/user_ldap && tar xfz user_ldap.tar.gz -C
/var/www/owncloud/apps/user_ldap --strip-components 1 && rm -f
user_ldap.tar.gz  
  
RUN curl -sLo activity.tar.gz
https://github.com/owncloud/activity/releases/download/v2.3.6/activity-v2.3.6.tar.gz
&& echo "f7bf0cc74213e7db08cb35daab3ed01c3efe83ee4f04bb4e4b1ac219c089c9e4
activity.tar.gz" | sha256sum -c - && mkdir -p /var/www/owncloud/apps/activity
&& tar xfz activity.tar.gz -C /var/www/owncloud/apps/activity --strip-
components 1 && rm -f activity.tar.gz  
  
RUN curl -sLo calendar.tar.gz
https://github.com/owncloud/calendar/releases/download/v1.5.4/calendar-v1.5.4.tar.gz
&& echo "35089183726eb5e0bc7a5ba89d3dbcb68932b0e222b0c4ecca017c6a9b1de068
calendar.tar.gz" | sha256sum -c - && mkdir -p /var/www/owncloud/apps/calendar
&& tar xfz calendar.tar.gz -C /var/www/owncloud/apps/calendar --strip-
components 1 && rm -f calendar.tar.gz  
  
RUN ( test -r /contacts-1.5.2.tar.gz && mv -f /contacts-1.5.2.tar.gz
contacts.tar.gz && echo
"4c2387ce249a9700b5d5b65570f35bb36ecc456ac01bbf66e74defa824169dfd
contacts.tar.gz" | sha256sum -c - && mkdir -p /var/www/owncloud/apps/contacts
&& tar xfz contacts.tar.gz -C /var/www/owncloud/apps/contacts --strip-
components 1 && rm -f contacts.tar.gz ) || echo "contacts app not found, put
it into data/apps/contacts/"  
  
RUN find /var/www/owncloud \\( \\! -user www-data -o \\! -group www-data \\)
-print0 | xargs -r -0 chown www-data:www-data  
  
FROM owncloud/base:latest  
MAINTAINER neffets <software@neffets.de>  
  
RUN apt-get update && apt-get install -y php-imap && phpenmod imap && apt-get
clean all;  
  
COPY \--from=build /var/www/owncloud/apps/ /var/www/owncloud/apps/  
  
LABEL org.label-schema.version=10.0.3  
LABEL org.label-schema.build-date=2017-11-10T13:51:35Z  
LABEL org.label-schema.vcs-ref=59d7d66  
LABEL org.label-schema.vcs-url="https://github.com/neffets/docker-owncloud-
server.git"  
LABEL org.label-schema.name="ownCloud Server"  
LABEL org.label-schema.vendor="neffets"  
LABEL org.label-schema.schema-version="1.0"  

