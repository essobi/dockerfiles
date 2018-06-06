FROM centos:centos7  
  
# Install Collabora, libmapuid and dumb-init  
RUN yum -y --setopt=tsflags=nodocs install wget openssl epel-release yum-utils
lsof netstat strace && \  
rpm --import https://www.collaboraoffice.com/repos/CollaboraOnline/CODE-
centos7/repodata/repomd.xml.key && \  
yum-config-manager --add-repo
https://www.collaboraoffice.com/repos/CollaboraOnline/CODE-centos7 && \  
yum -y --setopt=tsflags=nodocs --nogpgcheck install loolwsd CODE-brand nginx
&& \  
wget -O /usr/local/sbin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 && \  
chmod +x /usr/local/sbin/dumb-init && \  
curl
https://raw.githubusercontent.com/appuio/libmapuid/master/lib/libmapuid.so -o
/usr/local/lib/libmapuid.so && \  
chmod 755 /usr/local/lib/libmapuid.so && \  
echo "/usr/local/lib/libmapuid.so" > /etc/ld.so.preload && \  
yum clean all  
  
# Setup directories and permissions - prepare for libmapuid  
RUN usermod -u 1001 lool && \  
mkdir /home/lool && \  
directories="/home/lool /etc/loolwsd /var/cache/loolwsd /opt/lool" && \  
chown -R lool:root $directories && \  
chmod -R g+rwX $directories  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
# be backwards compatible with pre-official images  
RUN ln -sf ../share/nginx /usr/local/nginx  
  
COPY nginx.conf /etc/nginx/nginx.conf  
RUN mkdir -p /var/cache/nginx && \  
chown -R 1001:0 /var/cache/nginx && \  
chmod -R a+rwx /var/cache/nginx && \  
chmod -R ug+rwx /var/cache/nginx  
  
ADD entrypoint.sh /  
COPY loolwsd.xml /etc/loolwsd/loolwsd.xml  
  
USER 1001  
EXPOSE 8080  
ENTRYPOINT ["dumb-init", "/entrypoint.sh"]  
CMD ["loolwsd"]  
CMD ["nginx"]  
  

