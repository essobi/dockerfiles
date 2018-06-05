#  
# meedan/acme.sh  
#  
# based on  
# https://github.com/m31271n/docker-acme.sh/blob/master/Dockerfile  
FROM meedan/base  
MAINTAINER sysops@meedan.com  
  
# Internal  
ENV LE_WORKING_DIR=/acme \  
TEMP_DIR=/tmp/acme_sh \  
CERT_DIR=/certs \  
ACCOUNT_DIR=/account \  
ACMEUSER=acme  
  
COPY docker_entrypoint.sh /docker_entrypoint.sh  
  
RUN useradd ${ACMEUSER}  
RUN git clone \--depth 1 https://github.com/Neilpang/acme.sh.git ${TEMP_DIR} \  
&& mkdir -p ${CERT_DIR} ${ACCOUNT_DIR} ${LE_WORKING_DIR}/ca/acme-
staging.api.letsencrypt.org ${LE_WORKING_DIR}/ca/acme-v01.api.letsencrypt.org
\  
&& chown -R ${ACMEUSER}:${ACMEUSER} ${LE_WORKING_DIR} \  
&& cd ${TEMP_DIR} \  
&& gosu ${ACMEUSER} ./acme.sh --install \  
\--home ${LE_WORKING_DIR} \  
\--certhome ${CERT_DIR} \  
\--accountkey ${ACCOUNT_DIR}/account.key \  
\--useragent "acme.sh in docker" \  
&& ln -s ${LE_WORKING_DIR}/acme.sh /usr/local/bin \  
&& rm -rf ${TEMP_DIR}  
  
VOLUME $CERT_DIR  
VOLUME $ACCOUNT_DIR  
  
USER ${ACMEUSER}  
ENTRYPOINT ["/docker_entrypoint.sh"]  

