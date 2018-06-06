FROM debian:stretch  
  
MAINTAINER Dmitrii Zolotov <dzolotov@herzen.spb.ru>  
  
RUN groupadd -r ldap && useradd -r -g ldap ldap  
  
RUN mkdir -p /opt/reopenldap/var/run/slapd/  
  
RUN cd /opt/ && apt-get -y update && apt install -y wget build-essential && \  
wget
"https://downloads.sourceforge.net/project/openslp/2.0.0/2.0.0%20Release/openslp-2.0.0.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fopenslp%2Ffiles%2F&ts=1506792295&use_mirror=10gbps-
io" && \  
tar xzvpf openslp* && cd openslp-2.0.0 && ./configure && make && make install  
  
RUN apt-get -y update \  
&& LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-
recommends \  
libsasl2-modules \  
libsasl2-modules-db \  
libsasl2-modules-gssapi-mit \  
libsasl2-modules-ldap \  
libsasl2-modules-otp \  
libsasl2-modules-sql \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD *.patch /opt  
  
RUN apt-get update -qq && apt-get install -yqq --no-install-recommends
gettext-base \  
git automake uuid-dev bc libelf-dev pkg-config libgnutls30 libgnutlsxx28
libgnutls28-dev libsasl2-dev libdb5.3-dev strace libelf-dev libbfd-dev gdb \  
groff file libltdl-dev libltdl7 libmagic1 libtool libkrb5-dev man ca-
certificates libperl-dev libsodium-dev && \  
git clone https://github.com/ReOpen/ReOpenLDAP.git /opt/reopenldap.source && \  
cd /opt/reopenldap.source && git checkout stable/1.1 && cp /opt/ordering.patch
servers/slapd/ && cd servers/slapd && patch -p0 <ordering.patch && cd ../.. &&
./bootstrap.sh && \  
./configure --with-tls=gnutls --enable-slapi --enable-ipv6=no --enable-
experimental=no --enable-local --enable-contrib=yes --enable-dynacl=yes
--enable-aci=yes --enable-spasswd=yes --enable-rewrite=yes --enable-mdb=yes
--enable-accesslog=yes --enable-auditlog=yes --enable-constraint=yes --enable-
dds=yes --enable-deref=yes --enable-memberof=yes --enable-ppolicy=yes
--enable-pcache=yes --enable-refint=yes --enable-rwm=yes --enable-seqmod=yes
--enable-sssvlv=yes --enable-syncprov=yes --enable-unique=yes --enable-
valsort=yes && \  
make -j ${NPROC} && make install && cd /opt/reopenldap && \  
rm -rf /opt/reopenldap.source && \  
apt-get remove -qq -y --purge automake build-essential libssl-dev libsasl2-dev
git \  
groff imagemagick cpp gcc cpp libtool libmagic1 && \  
apt-get autoremove -y -qq --purge && apt-get clean && chown ldap:ldap -R
/opt/reopenldap && apt-get purge -y libldap*  
  
ENV MANPATH /opt/reopenldap/share/man:/usr/share/man  
  
RUN mandb -u  
  
ENV PATH /opt/reopenldap/bin:/opt/reopenldap/sbin:$PATH  
  
WORKDIR /opt/reopenldap  
  
RUN mkdir -p /opt/reopenldap/var/run/slapdp /opt/reopenldap/var/reopenldap-
data && \  
chown ldap:ldap -R /opt/reopenldap/var  
  
ADD ldif/*.ldif /opt/  
  
ADD entrypoint.sh /opt  
  
# Expose default ldap and ldaps ports  
EXPOSE 389 636  
VOLUME /opt/reopenldap/var/reopenldap-data /opt/reopenldap/etc/slapd.d /cache
/opt/reopenldap/var/accesslog  
  
CMD /opt/entrypoint.sh  

