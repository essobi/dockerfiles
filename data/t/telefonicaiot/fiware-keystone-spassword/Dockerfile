FROM centos:centos7  
  
MAINTAINER IoT team  
  
ENV DB_HOST localhost  
ENV KEYSTONE_ADMIN_PASSWORD 4pass1w0rd  
ENV KEYSTONE_SCIM_VERSION 1.1.8  
ENV KEYSTONE_SPASSWORD_VERSION 1.5.0  
  
COPY ./*.sh /opt/keystone/  
COPY ./*.patch /opt/keystone/  
COPY ./sql_ldap.py /opt/keystone/  
  
WORKDIR /opt/keystone  
  
RUN \  
# Install dependencies  
yum update -y && yum install -y curl && \  
yum install -y epel-release && yum update -y epel-release && \  
# Install MySQL client  
yum -y install mysql git && \  
# Install keystone dependencies  
yum -y install rpm-build tar findutils && \  
yum -y install python && \  
curl -s \--insecure -L
'https://repos.fedorapeople.org/openstack/EOL/openstack-mitaka/rdo-release-
mitaka-7.noarch.rpm?raw=true' > rdo-release-mitaka-7.noarch.rpm && \  
yum localinstall -y \--nogpgcheck rdo-release-mitaka-7.noarch.rpm && \  
# Set Centos mirror to ctinetworks to ensure openstack Mitaka version  
sed -i 's/mirror.centos.org/distro.ctinetworks.com\/mirror/g'
/etc/yum.repos.d/rdo-release.repo && \  
# Install keystone dependencies  
yum -y install openstack-utils openstack-keystone python-keystoneclient && \  
yum -y install unzip tcping jq && \  
yum -y install cracklib cracklib-python && \  
# Set keystone configuration  
openstack-config \--set /etc/keystone/keystone.conf \  
database connection mysql://keystone:keystone@db/keystone && \  
openstack-config \--set /etc/keystone/keystone.conf \  
DEFAULT admin_token ADMIN && \  
openstack-config \--set /etc/keystone/keystone.conf \  
DEFAULT public_port 5001 && \  
openstack-config \--set /etc/keystone/keystone.conf \  
os_inherit enabled true && \  
openstack-config \--set /etc/keystone/keystone.conf \  
database connection mysql://keystone:keystone@$DB_HOST/keystone && \  
# Set keystone SSL configuration  
openstack-config \--set /etc/keystone/keystone.conf \  
token provider keystone.token.providers.uuid.Provider && \  
keystone-manage pki_setup \--keystone-user keystone \--keystone-group keystone
&& \  
chown -R keystone:keystone /etc/keystone/ssl && \  
chmod -R o-rwx /etc/keystone/ssl && \  
# Create /opt/keystone  
mkdir -p /opt/keystone && \  
# Keystone postconfig file  
chmod 755 /opt/keystone/postlaunchconfig.sh
/opt/keystone/postlaunchconfig_update.sh /opt/keystone/keystone-entrypoint.sh
&& \  
# chown root.root /opt/keystone/postlaunchconfig.sh
/opt/keystone/postlaunchconfig_update.sh /opt/keystone/keystone-entrypoint.sh
&& \  
ln -s /etc/keystone/keystone-paste.ini /usr/share/keystone/keystone-dist-
paste.ini && \  
# Install Keystone-SCIM  
tag=$KEYSTONE_SCIM_VERSION && \  
user="telefonicaid" && \  
repo_scim="fiware-keystone-scim" && \  
pack_scim="package-keystone-scim.sh" && \  
url_scim="https://github.com/${user}/${repo_scim}/archive/${tag}.tar.gz" && \  
dir=~/fiware-keystone && \  
rm -fR $dir && mkdir -p $dir && \  
curl -s \--insecure -L "${url_scim}" | tar zxvf - -C ${dir} && \  
cd ${dir}/${repo_scim}-${tag} && \  
source ./${pack_scim} \--with-python27 \--with-version $KEYSTONE_SCIM_VERSION
\--with-release 0 && \  
find . -name "*.rpm" -exec rpm -Uvh {} \; && \  
# Install Keystone-SPASSWORD  
cd /opt/keystone && \  
tag=$KEYSTONE_SPASSWORD_VERSION && \  
user="telefonicaid" && \  
repo_spassword="fiware-keystone-spassword" && \  
pack_spassword="package-keystone-spassword.sh" && \  
url_spassword="https://github.com/${user}/${repo_spassword}/archive/${tag}.tar.gz"
&& \  
dir=~/fiware-keystone && \  
rm -fR $dir && mkdir -p $dir && \  
curl -s \--insecure -L "${url_spassword}" | tar zxvf - -C ${dir} && \  
cd ${dir}/${repo_spassword}-${tag} && \  
source ./${pack_spassword} \--with-python27 \--with-version
$KEYSTONE_SPASSWORD_VERSION \--with-release 0 && \  
find . -name "*.rpm" -exec rpm -Uvh {} \; && \  
# Patching Mitaka to enable extra fields in token response  
cd /usr/lib/python2.7/site-packages/keystone/token/providers && \  
patch -f -p0 < /opt/keystone/common.patch && \  
# LDAP pre-support  
mkdir -p /etc/keystone/domains && \  
chown keystone.keystone /etc/keystone/domains && \  
openstack-config \--set /etc/keystone/keystone.conf \  
identity domain_specific_drivers_enabled true && \  
openstack-config \--set /etc/keystone/keystone.conf \  
identity domain_config_dir /etc/keystone/domains && \  
cp /opt/keystone/sql_ldap.py /usr/lib/python2.7/site-
packages/keystone/identity/mapping_backends && \  
openstack-config \--set /etc/keystone/keystone.conf \  
identity_mapping driver keystone.identity.mapping_backends.sql_ldap.Mapping &&
\  
# Cleaning unused files...  
rpm -e \--nodeps redhat-logos || true && yum -y erase libss && \  
yum clean all && rm -rf /var/lib/yum/yumdb && \  
rm -rf /var/lib/yum/history && find /usr/share/locale -mindepth 1 -maxdepth 1
! -name 'en' ! -name 'es' ! -name 'es_ES' | xargs rm -r && \  
rm -rf ~/fiware-keystone && rm -f /var/log/*log && rm -f /opt/keystone/*.rpm  
# Define the entry point  
ENTRYPOINT ["/opt/keystone/keystone-entrypoint.sh"]  
  
EXPOSE 5001  
  

