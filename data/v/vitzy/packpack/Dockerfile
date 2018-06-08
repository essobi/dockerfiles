FROM opensuse:42.3  
MAINTAINER Ahmed Zetao Yang <yangzetao2015@outlook.com>  
  
# Fix missing locales  
ENV LC_ALL="C.UTF-8" LANG="C.UTF-8"  
# Enable extra repositories  
RUN zypper -n ref && \  
zypper -n up --skip-interactive --no-recommends && \  
zypper -n install -l --no-recommends \  
wget \  
curl \  
ca-certificates \  
python-gnupg \  
yum-utils && \  
zypper clean && \  
rm -rf /var/cache/zypp/*  
  
# Install base toolset  
RUN zypper -n up --skip-interactive && zypper -n install \  
sudo \  
git \  
patterns-openSUSE-devel_basis \  
cmake \  
gdb \  
ccache \  
fakeroot \  
rpm \  
rpm-build \  
rpmdevtools \  
yast2-packager  
  
# Enable cache system-wide  
ENV PATH
/usr/lib/ccache:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin  
  
# Enable sudo without tty  
RUN sed -i.bak -n -e '/^Defaults.*requiretty/ { s/^/# /;};/^%wheel.*ALL$/ {
s/^/# / ;} ;/^#.*wheel.*NOPASSWD/ { s/^#[ ]*//;};p' /etc/sudoers  

