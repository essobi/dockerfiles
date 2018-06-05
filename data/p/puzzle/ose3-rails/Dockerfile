FROM centos/ruby-24-centos7  
  
LABEL io.k8s.description="Base Image for Rails" \  
io.k8s.display-name="pitc-rails-bi" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,ruby,ruby22,httpd"  
  
# ABOUT  
# A Rails image to be used with OpenShift S2I.  
USER root  
ENV RUBY_MAJOR 2.4  
ENV RUBY_VERSION 2.4.4  
ENV BUNDLER_VERSION 1.15.0  
ENV RUBYGEMS_VERSION 2.6.12  
RUN \  
/bin/bash -c "yum -y remove rh-ruby24*" \  
&& sed -i 's/\<rh-ruby24\>//g' /opt/app-root/etc/scl_enable \  
&& yum -y groupinstall --setopt=tsflags=nodocs 'Development Tools' \  
&& yum -y update \  
&& yum -y install --setopt=tsflags=nodocs \  
libyaml-devel \  
openssl \  
openssl-devel \  
gdbm-devel \  
libffi-devel \  
gmp-devel \  
readline-devel \  
wget \  
&& yum clean all \  
&& wget https://cache.ruby-
lang.org/pub/ruby/$RUBY_MAJOR/ruby-$RUBY_VERSION.tar.gz \  
&& tar xzf ruby-$RUBY_VERSION.tar.gz -C /usr/src \  
&& cd /usr/src/ruby-$RUBY_VERSION \  
&& CFLAGS="-O3 -fPIC -fno-strict-aliasing" ./configure --disable-install-doc
--enable-shared --enable-pthread \  
&& make \  
&& make install \  
&& cd / \  
&& rm -rf /usr/src/ruby-$RUBY_VERSION \  
&& rm -rf /ruby-$RUBY_VERSION.tar.gz \  
&& gem update --system "$RUBYGEMS_VERSION" \  
&& gem install bundler --version "$BUNDLER_VERSION" \  
&& yum clean all  
USER root  
  
# SLOW STUFF  
# Slow operations, kept at top of the Dockerfile so they're cached for most
changes.  
# Install Apache httpd24.  
RUN yum update -y && \  
INSTALL_PKGS="httpd httpd-devel apr-devel apr-util-devel sqlite3 ImageMagick-
devel" && \  
yum install -y --setopt=tsflags=nodocs $INSTALL_PKGS && \  
yum clean all -y  
  
# Install passenger.  
#  
# We pin passenger to a minor version because the automatic upgrade from  
# 5.1 -> 5.2 broke all our apps.  
RUN /bin/bash -c "gem install passenger -v '~> 5.1.12' --no-ri --no-rdoc && \  
passenger-install-apache2-module --auto --languages ruby && \  
passenger-config validate-install " # bogus comment to invalidate cache  
  
# CONFIGURATION  
### Apache  
# Disable digest_module.  
RUN sed -i "s/LoadModule auth_digest_module/#LoadModule auth_digest_module/"
/etc/httpd/conf.modules.d/00-base.conf  
ENV APACHE_RUN_USER 1001  
ENV APACHE_PID_FILE /opt/app-root/httpd.pid  
# TODO Why do we do this? I suspect it's because of the OpenShift PID hack for
apache.  
RUN mkdir -p /opt/app-root/httpd/pid  
  
### Passenger  
# Add a symlink to the installed passenger gem  
# so we do not depend on the minor version installed.  
RUN ln -s /usr/local/lib/ruby/gems/*/gems/passenger-5.* /opt/passenger  
  
### Rails  
ENV RAILS_ENV=production \  
RAILS_ROOT=/opt/app-root/src  
  
### Add configuration files.  
ADD /contrib/bin $STI_SCRIPTS_PATH  
ADD /contrib/etc/httpd /etc/httpd  
ADD /contrib/usr/local/lib /usr/local/lib  
  
# PERMISSIONS  
# TODO Why do we do this? Check with the fix-permissions call in
$STI_SCRIPTS_PATH/assemble.  
RUN chgrp -R 0 ./ && \  
chmod -R g+rw ./ && \  
find ./ -type d -exec chmod g+x {} + && \  
chown -R 1001:0 ./  
  
# TODO Why do we do this? Check with the fix-permissions call in
$STI_SCRIPTS_PATH/assemble.  
RUN chmod -R a+rwX /opt/app-root/httpd/pid && \  
chmod +x $STI_SCRIPTS_PATH/run-httpd.sh  
  
# Workaround for base image: Do not install gems from development and test
environments  
# See https://github.com/sclorg/rhscl-dockerfiles/issues/26  
ENV BUNDLE_WITHOUT=development:test  
  
# Add S2I scripts.  
USER root  
  
RUN mv $STI_SCRIPTS_PATH/assemble $STI_SCRIPTS_PATH/assemble_base  
RUN mv $STI_SCRIPTS_PATH/run $STI_SCRIPTS_PATH/run_base  
ADD /s2i/* $STI_SCRIPTS_PATH/  
  
RUN chmod ugo+x $STI_SCRIPTS_PATH/*  
  
USER 1001  
USER 1001  
# ENTRYPOINT  
CMD $STI_SCRIPTS_PATH/run-httpd.sh  

