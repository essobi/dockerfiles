FROM opensuse/tumbleweed  
  
# do not install the files marked as documentation (use "rpm --excludedocs")  
RUN sed -i -e "s/^.*rpm.install.excludedocs.*/rpm.install.excludedocs = yes/"
/etc/zypp/zypp.conf  
  
# "zypper dup" synchronizes with the current Tumbleweed (even downgrades if
needed),  
# we need to install Ruby first to define the %{rb_default_ruby_abi} RPM macro  
# and curl for downloading/installing the GPG key  
# see https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/#run  
# https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-
practices/#/build-cache  
# why we need "zypper clean -a" at the end  
RUN zypper --non-interactive dup --no-recommends && \  
zypper --non-interactive in \--no-recommends curl ruby && \  
zypper clean -a  
  
# import the YaST OBS GPG key  
RUN rpm --import https://build.opensuse.org/projects/YaST/public_key  
  
RUN zypper ar -f
https://download.opensuse.org/repositories/YaST:/Head/openSUSE_Tumbleweed/
yast  
  
RUN RUBY_VERSION=ruby:`rpm --eval '%{rb_ver}'` && \  
zypper --non-interactive in \--no-recommends \  
aspell-en \  
fdupes \  
git \  
grep \  
rpm-build \  
update-desktop-files \  
which \  
libxml2-tools \  
libxslt-tools \  
"rubygem($RUBY_VERSION:abstract_method)" \  
"rubygem($RUBY_VERSION:cfa)" \  
"rubygem($RUBY_VERSION:cheetah)" \  
"rubygem($RUBY_VERSION:coveralls)" \  
"rubygem($RUBY_VERSION:gettext)" \  
"rubygem($RUBY_VERSION:parallel)" \  
"rubygem($RUBY_VERSION:raspell)" \  
"rubygem($RUBY_VERSION:rspec)" \  
"rubygem($RUBY_VERSION:rubocop)" \  
"rubygem($RUBY_VERSION:simplecov)" \  
"rubygem($RUBY_VERSION:simpleidn)" \  
"rubygem($RUBY_VERSION:suse-connect)" \  
"rubygem($RUBY_VERSION:yard)" \  
"rubygem($RUBY_VERSION:yast-rake)" \  
build \  
obs-service-source_validator \  
patterns-rpm-macros \  
yast2 \  
yast2-add-on \  
yast2-bootloader \  
yast2-core \  
yast2-country \  
yast2-devtools \  
yast2-hardware-detection \  
yast2-inetd \  
yast2-installation \  
yast2-installation-control \  
yast2-ldap \  
yast2-network \  
yast2-nfs-server \  
yast2-packager \  
yast2-pam \  
yast2-perl-bindings \  
yast2-pkg-bindings \  
yast2-proxy \  
yast2-ruby-bindings \  
yast2-samba-client \  
yast2-security \  
yast2-services-manager \  
yast2-slp \  
yast2-storage-ng \  
yast2-testsuite \  
yast2-transfer \  
yast2-update \  
yast2-users \  
yast2-xml \  
yast2-ycp-ui-bindings \  
&& zypper clean -a \  
&& rm -rf /usr/lib*/ruby/gems/*/cache/ \  
&& rm -rf /usr/share/doc/  
  
COPY yast-travis-ruby /usr/local/bin/  
ENV LC_ALL=en_US.UTF-8  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# just some smoke tests, make sure rake and YaST work properly,  
# ensure there is no leftover in the working directory  
RUN rake -r yast/rake -V && TERM=xterm yast2 proxy summary && \  
rm -rf /var/log/YaST2/y2log && rm -rf /usr/src/app/*  

