FROM centos:6.9  
LABEL maintainer "ine1127"  
  
ENV CONST_LDAP_HOME_DIR="/home/ldap" \  
CONST_LDAP_USER="ldap" \  
CONST_LDAP_GROUP="ldap" \  
CONST_LDAP_UID="55" \  
CONST_LDAP_GID="55"  
ENV CONST_LDAP_DATA_DIR="${CONST_LDAP_HOME_DIR}/openldap" \  
CONST_LDAP_RUNTIME_DIR="${CONST_LDAP_HOME_DIR}/runtime" \  
CONST_LDAP_WORK_DIR="${CONST_LDAP_HOME_DIR}/work"  
ENV CONST_LDAP_BACKUP_DIR="${CONST_LDAP_DATA_DIR}/backup" \  
CONST_LDAP_CERTS_DIR="${CONST_LDAP_DATA_DIR}/certs" \  
CONST_LDAP_CONFIG_DIR="${CONST_LDAP_DATA_DIR}/slapd.d" \  
CONST_LDAP_DBDATA_DIR="${CONST_LDAP_DATA_DIR}/dbdata"  
ENV CONST_LDAP_NSSDB_NOISE="${CONST_LDAP_CERTS_DIR}/noise" \  
CONST_LDAP_NSSDB_PASS="${CONST_LDAP_CERTS_DIR}/password"  
COPY entrypoint.sh /usr/local/sbin/entrypoint.sh  
  
RUN groupadd \  
-g "${CONST_LDAP_GID}" "${CONST_LDAP_GROUP}" && \  
useradd \  
-g "${CONST_LDAP_GROUP}" \  
-u "${CONST_LDAP_UID}" \  
-d "${CONST_LDAP_HOME_DIR}" \  
-s "/bin/bash" \  
-c "LDAP User" \  
"${CONST_LDAP_USER}" && \  
  
yum -y update && \  
yum -y install \  
openldap-clients \  
openldap-servers \  
epel-release && \  
yum -y install lmdb && \  
yum clean all && \  
  
rm -rf /etc/openldap/slapd.d/* && \  
runuser -m -s /bin/mkdir -- "${CONST_LDAP_USER}" \  
"${CONST_LDAP_WORK_DIR}" "${CONST_LDAP_DATA_DIR}" && \  
chmod 755 /usr/local/sbin/entrypoint.sh  
  
COPY runtime/ "${CONST_LDAP_RUNTIME_DIR}"  
  
EXPOSE 10389/tcp 10636/tcp  
  
USER "${CONST_LDAP_USER}"  
WORKDIR "${CONST_LDAP_HOME_DIR}"  
  
VOLUME ["${CONST_LDAP_DATA_DIR}"]  
  
ENTRYPOINT ["/usr/local/sbin/entrypoint.sh"]  
CMD ["start"]  

