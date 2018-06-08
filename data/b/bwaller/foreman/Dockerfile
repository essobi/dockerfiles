FROM bwaller/foreman-base  
  
MAINTAINER B Waller bjorn@waller.nu  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PUPPET_ENVS_DIR /etc/puppet/environments  
ENV DB_USERNAME foreman  
ENV DB_PASSWORD changeme  
ENV DB_HOST localhost  
  
ENV FOREMANOPTS --enable-foreman \  
--no-enable-foreman-compute-ec2 \  
--enable-foreman-compute-libvirt \  
--no-enable-foreman-compute-openstack \  
--no-enable-foreman-compute-ovirt \  
--no-enable-foreman-compute-rackspace \  
--enable-foreman-compute-vmware \  
--enable-foreman-plugin-setup \  
--enable-foreman-plugin-templates \  
--enable-foreman-plugin-puppetdb \  
--enable-foreman-proxy \  
--enable-puppet \  
--foreman-authentication=true \  
--foreman-admin-username=admin \  
--foreman-admin-password=changeme \  
--foreman-db-manage=true \  
--foreman-db-type=postgresql \  
--foreman-proxy-dns=true \  
--foreman-proxy-dns-server=192.168.10.20 \  
--foreman-proxy-tftp=true \  
--puppet-server-envs-dir=$PUPPET_ENVS_DIR \  
--puppet-show-diff=true  
  
EXPOSE 443  
EXPOSE 8140  
EXPOSE 8443  
  
CMD ( test ! -f /etc/foreman/.first_run_completed && \  
( echo "FIRST-RUN: Please wait while Foreman is installed and configured...";
\  
/usr/sbin/foreman-installer $FOREMANOPTS \  
--foreman-db-username=$DB_USERNAME \  
--foreman-db-password=$DB_PASSWORD; \  
touch /etc/foreman/.first_run_completed \  
) \  
); \  
/etc/init.d/puppet stop; \  
/etc/init.d/httpd stop; \  
/etc/init.d/foreman-proxy stop; \  
/etc/init.d/foreman stop; \  
/etc/init.d/postgresql stop; \  
/etc/init.d/postgresql start; \  
/etc/init.d/foreman start; \  
/etc/init.d/foreman-proxy start; \  
/etc/init.d/httpd start; \  
/etc/init.d/puppet start; \  
tail -f /var/log/foreman/production.log  

