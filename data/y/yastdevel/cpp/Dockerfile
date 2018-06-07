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
screen \  
"rubygem($RUBY_VERSION:coveralls)" \  
"rubygem($RUBY_VERSION:fast_gettext)" \  
"rubygem($RUBY_VERSION:gettext)" \  
"rubygem($RUBY_VERSION:raspell)" \  
"rubygem($RUBY_VERSION:rspec)" \  
"rubygem($RUBY_VERSION:rubocop)" \  
"rubygem($RUBY_VERSION:simplecov)" \  
"rubygem($RUBY_VERSION:yard)" \  
"rubygem($RUBY_VERSION:yast-rake)" \  
autoconf \  
automake \  
bison \  
boost-devel \  
cmake \  
dejagnu \  
docbook-xsl-stylesheets \  
doxygen \  
flex \  
gcc-c++ \  
libtool \  
libxslt \  
build \  
obs-service-source_validator \  
ruby-devel \  
sgml-skel \  
yast2-devtools \  
yast2-core-devel \  
yast2-devtools \  
hwinfo-devel \  
yast2-ycp-ui-bindings-devel \  
&& zypper clean -a \  
&& rm -rf /usr/lib*/ruby/gems/*/cache/ \  
&& rm -rf /usr/share/doc/  
  
COPY yast-travis-cpp /usr/local/bin/  
ENV LC_ALL=en_US.UTF-8  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# run some smoke tests to make sure there is no serious issue with the image  
RUN /usr/lib/YaST2/bin/y2base --help && c++ --version && rake -r yast/rake -V  

