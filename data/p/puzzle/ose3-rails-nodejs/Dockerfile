FROM centos/ruby-22-centos7  
# ABOUT  
# A Rails/webpack frontend image to be used with S2I.  
#  
# * nodejs, npm and yarn will get installed  
# * the assets at frontend/dist are moved to public/  
USER root  
  
# SLOW STUFF  
# Slow operations, kept at top of the Dockerfile so they're cached for most
changes.  
# Install Apache httpd24, mod_xsendfile, mod_ssl and build deps  
RUN yum -y install epel-release && \  
yum update -y && \  
INSTALL_PKGS="httpd httpd-devel mod_xsendfile mod_ssl apr-devel apr-util-devel
sqlite3 ImageMagick-devel" && \  
yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \  
yum clean all -y  
  
# Install passenger.  
#  
# We pin passenger to a minor version because the automatic upgrade from  
# 5.1 -> 5.2 broke all our apps.  
RUN /bin/bash -c "gem install passenger -v '~> 5.1.12' --no-ri --no-rdoc && \  
export PATH=$PATH:/opt/rh/rh-ruby22/root/usr/local/bin && \  
passenger-install-apache2-module --auto --languages ruby && \  
passenger-config validate-install "  
  
# CONFIGURATION  
### Apache  
# Disable digest_module.  
RUN \  
sed -i "s/LoadModule auth_digest_module/#LoadModule auth_digest_module/"
/etc/httpd/conf.modules.d/00-base.conf && \  
# TODO Why do we do this mkdir thing?  
# I suspect it's because of the OpenShift PID hack for apache.  
mkdir -p /opt/app-root/httpd/pid && \  
# Target directories for app-provided httpd configuration  
mkdir /etc/httpd/app_provided.d && \  
chmod go+rwx /etc/httpd/app_provided.d && \  
# remove default config that we replace  
rm /etc/httpd/conf.d/ssl.conf  
  
ENV APACHE_RUN_USER 1001  
ENV APACHE_PID_FILE /opt/app-root/httpd.pid  
  
### Passenger  
# Add a symlink to the installed passenger gem  
# so we do not depend on the minor version installed.  
RUN ln -s /opt/rh/rh-ruby22/root/usr/local/share/gems/gems/passenger-5.*
/opt/passenger  
ENV PASSENGER_START_TIMEOUT=90 \  
PASSENGER_MIN_INSTANCES=2 \  
PASSENGER_MAX_POOL_SIZE=6 \  
PASSENGER_PRE_START_PATH="/"  
### Rails  
ENV RAILS_ENV=production \  
RAILS_ROOT=/opt/app-root/src  
  
### Add configuration files.  
ADD /contrib/bin $STI_SCRIPTS_PATH  
ADD /contrib/etc/httpd /etc/httpd  
ADD /contrib/usr/local/lib /usr/local/lib  
  
# PERMISSIONS  
RUN \  
# Allow moving feature config files to conf.d in run-httpd.sh  
chmod go+rwx /etc/httpd/features /etc/httpd/conf.d && \  
# TODO Why do we do this?  
# Check with the fix-permissions call in $STI_SCRIPTS_PATH/assemble.  
chgrp -R 0 ./ && \  
chmod -R g+rw ./ && \  
find ./ -type d -exec chmod g+x {} + && \  
chown -R 1001:0 ./ && \  
chmod -R a+rwX /opt/app-root/httpd/pid && \  
chmod +x $STI_SCRIPTS_PATH/run-httpd.sh  
  
# Workaround for base image: Do not install gems from development and test
environments  
# See https://github.com/sclorg/rhscl-dockerfiles/issues/26  
ENV BUNDLE_WITHOUT=development:test  
  
USER root  
  
ADD /contrib/bin/install-nodejs $STI_SCRIPTS_PATH  
  
RUN \  
# Remove nodejs provided by centos ruby22 base image  
yum remove -y rh-nodejs* && \  
sed -e "s/ \$NODEJS_SCL//g" -i /opt/app-root/etc/scl_enable && \  
# Install node  
scl enable rh-ruby22 $STI_SCRIPTS_PATH/install-nodejs && \  
# Install yarn (install without dep check since nodejs is installed via tar)  
wget https://dl.yarnpkg.com/rpm/yarn.repo -O /etc/yum.repos.d/yarn.repo && \  
rpm -Uvh --nodeps $(repoquery --location yarn)  
  
ENV PATH="/opt/nodejs/bin:${PATH}"  
# Add S2I scripts.  
USER root  
  
RUN mv $STI_SCRIPTS_PATH/assemble $STI_SCRIPTS_PATH/assemble_base  
RUN mv $STI_SCRIPTS_PATH/run $STI_SCRIPTS_PATH/run_base  
ADD /s2i/* $STI_SCRIPTS_PATH/  
  
RUN chmod ugo+x $STI_SCRIPTS_PATH/*  
  
USER 1001  
# ENTRYPOINT  
CMD $STI_SCRIPTS_PATH/run-httpd.sh

