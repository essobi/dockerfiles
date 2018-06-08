FROM fedora:22  
MAINTAINER Michal Karm Babacek <karm@redhat.com>  
  
##  
## This is supposed to be a developer _toy_ Docker image one might  
## find useful while playing with mod_cluster smart load balancer.  
##  
## Constants  
# A git branch or a tag; whatever one finds on project's upstream GitHub.  
ENV HTTPD_BRANCH 2.4.17  
ENV APR_BRANCH 1.5.1  
ENV APR_UTIL_BRANCH 1.5.4  
ENV MOD_CLUSTER_BRANCH master  
  
# All 4 mod_cluster modules are required. Their names may vary across
versions.  
ENV MOD_CLUSTER_MODULES advertise mod_cluster_slotmem mod_manager
mod_proxy_cluster  
  
# The source of this Docker image build is reasonably transparent.  
ENV HTTPD_DIST https://github.com/apache/httpd/archive/${HTTPD_BRANCH}.zip  
ENV APR_DIST https://github.com/apache/apr/archive/${APR_BRANCH}.zip  
ENV APR_UTIL_DIST https://github.com/apache/apr-
util/archive/${APR_UTIL_BRANCH}.zip  
ENV MOD_CLUSTER_DIST
https://github.com/modcluster/mod_cluster/archive/${MOD_CLUSTER_BRANCH}.zip  
  
# Compile time dependencies we shall get rid off in the same layer where  
# the compilation takes place.  
ENV COMPILETIME_DEPS binutils libtool openssl-devel unzip make autoconf gcc
file which  
  
ENV HTTPD_MC_BUILD_DIR /opt/httpd-build  
  
# Meh...  
ENV CFLAGS -O2  
  
## Build  
# The idea is to manage the build in a single layer  
# and get rid of unnecessary artifacts as soon as it's done.  
WORKDIR /opt  
  
# OMG, ADD from URL runs always :-( Zips rest there unused. Let's go back to
wget.  
ADD ${HTTPD_DIST} ${APR_DIST} ${APR_UTIL_DIST} ${MOD_CLUSTER_DIST} /opt/  
  
# Note erratic indentation around ./configure. It's on purpose because of
http://goo.gl/DgDsbD  
RUN dnf -y update && dnf -y install iproute ${COMPILETIME_DEPS} && dnf clean
all  
RUN unzip ${HTTPD_BRANCH}.zip && rm -rf ${HTTPD_BRANCH}.zip && \  
unzip ${APR_BRANCH}.zip && mv apr-* httpd-${HTTPD_BRANCH}/srclib/apr && rm -rf
${APR_BRANCH}.zip && \  
unzip ${APR_UTIL_BRANCH}.zip && mv apr-util* httpd-${HTTPD_BRANCH}/srclib/apr-
util && rm -rf ${APR_UTIL_BRANCH}.zip && \  
unzip ${MOD_CLUSTER_BRANCH}.zip && rm -rf ${MOD_CLUSTER_BRANCH}.zip && \  
cd /opt/httpd-${HTTPD_BRANCH} && \  
./buildconf && ./configure --prefix=${HTTPD_MC_BUILD_DIR} \--with-mpm=worker
--enable-mods-shared=most \  
\--enable-maintainer-mode --with-expat=builtin \--enable-ssl --enable-proxy
--enable-proxy-http \  
\--enable-proxy-ajp --disable-proxy-balancer --with-threads \  
&& make && make install && \  
cd /opt/mod_cluster-${MOD_CLUSTER_BRANCH}/native && \  
for module in ${MOD_CLUSTER_MODULES};do cd $module; \  
./buildconf && ./configure --with-apxs=${HTTPD_MC_BUILD_DIR}/bin/apxs \  
&& make && make install && cp *.so ${HTTPD_MC_BUILD_DIR}/modules/ \  
&& cd ..; \  
done; \  
rm -rf /opt/httpd-${HTTPD_BRANCH} /opt/mod_cluster-${MOD_CLUSTER_BRANCH}  
  
## Test  
# Configuration and smoke test  
COPY mod_cluster.conf ${HTTPD_MC_BUILD_DIR}/conf/extra/mod_cluster.conf  
RUN cat ${HTTPD_MC_BUILD_DIR}/conf/extra/mod_cluster.conf  
RUN sed -i 's/LogLevel warn/LogLevel debug/g'
${HTTPD_MC_BUILD_DIR}/conf/httpd.conf && \  
echo "Include conf/extra/httpd-mpm.conf" >>
${HTTPD_MC_BUILD_DIR}/conf/httpd.conf && \  
echo "Include conf/extra/httpd-default.conf" >>
${HTTPD_MC_BUILD_DIR}/conf/httpd.conf && \  
echo "Include conf/extra/mod_cluster.conf" >>
${HTTPD_MC_BUILD_DIR}/conf/httpd.conf && \  
${HTTPD_MC_BUILD_DIR}/bin/apachectl start && sleep 5 && \  
cat ${HTTPD_MC_BUILD_DIR}/logs/error_log && \  
cat ${HTTPD_MC_BUILD_DIR}/conf/httpd.conf && \  
grep "Apache/" ${HTTPD_MC_BUILD_DIR}/logs/error_log && \  
grep "mod_cluster/.* configured -- resuming normal operations"
${HTTPD_MC_BUILD_DIR}/logs/error_log && \  
grep "update_workers_node starting" ${HTTPD_MC_BUILD_DIR}/logs/error_log && \  
[ "`grep -c 'error\|Segmentation fault\|Invalid argument\|mismatch detected'
${HTTPD_MC_BUILD_DIR}/logs/error_log`" -eq 0 ] && \  
${HTTPD_MC_BUILD_DIR}/bin/apachectl stop && \  
rm -rf ${HTTPD_MC_BUILD_DIR}/logs/* && rm -rf ${HTTPD_MC_BUILD_DIR}/cache/*  
  
EXPOSE 80/tcp  
EXPOSE 6666/tcp  
EXPOSE 23364/udp  
  
COPY docker-entrypoint.sh /  
#ensure the script is executable  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["start", "-DFOREGROUND"]  

