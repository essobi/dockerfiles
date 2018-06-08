FROM babim/alpinebase  
  
ENV SQUID_CACHE_DIR=/var/spool/squid \  
SQUID_LOG_DIR=/var/log/squid \  
SQUID_DIR=/squid \  
SQUID_CONFIG_DIR=/etc/squid \  
SQUID_USER=squid  
  
RUN apk add --no-cache squid bash apache2-utils \  
&& mv ${SQUID_CONFIG_DIR}/squid.conf ${SQUID_CONFIG_DIR}/squid.conf.dist  
  
COPY squid.conf ${SQUID_CONFIG_DIR}/squid.conf  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
RUN sed -i 's@#\tauth_param basic program /usr/lib/squid/basic_ncsa_auth
/usr/etc/passwd@auth_param basic program /usr/lib/squid/basic_ncsa_auth
/usr/etc/passwd\nacl ncsa_users proxy_auth REQUIRED@' /etc/squid/squid.conf  
RUN sed -i 's@^http_access allow localhost$@\0\nhttp_access allow ncsa_users@'
/etc/squid/squid.conf  
  
# change to one directory  
RUN [ -d ${SQUID_CACHE_DIR} ] || mkdir -p ${SQUID_CACHE_DIR} && \  
[ -d ${SQUID_LOG_DIR} ] || mkdir -p ${SQUID_LOG_DIR} && \  
[ -d ${SQUID_DIR} ] || mkdir -p ${SQUID_DIR} && mkdir -p ${SQUID_DIR}_start &&
\  
mv ${SQUID_CACHE_DIR} ${SQUID_DIR}_start/cache && ln -sf ${SQUID_DIR}/cache
${SQUID_CACHE_DIR} && \  
mv ${SQUID_LOG_DIR} ${SQUID_DIR}_start/log && ln -sf ${SQUID_DIR}/log
${SQUID_LOG_DIR} && \  
mv ${SQUID_CONFIG_DIR} ${SQUID_DIR}_start/config && ln -sf ${SQUID_DIR}/config
${SQUID_CONFIG_DIR}  
  
RUN mkdir /usr/etc  
  
EXPOSE 3128/tcp  
#VOLUME ["${SQUID_CACHE_DIR}", "${SQUID_LOG_DIR}", "${SQUID_CONFIG_DIR}"]  
VOLUME ["${SQUID_DIR}"]  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

