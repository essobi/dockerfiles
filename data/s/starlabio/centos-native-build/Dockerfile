FROM starlabio/centos-base:1.2  
MAINTAINER Doug Goldstein <doug@starlab.io>  
  
# setup linkers for Cargo  
RUN mkdir -p /root/.cargo/  
  
ENV PATH
"/root/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"  
# install rustup  
RUN curl https://sh.rustup.rs -sSf > rustup-install.sh && \  
sh ./rustup-install.sh -y --default-toolchain 1.24.1-x86_64-unknown-linux-gnu
&& \  
rm rustup-install.sh  
  
# Install rustfmt / cargo fmt for testing  
RUN cargo install --force rustfmt --vers 0.8.6  
  
# Install yum-plugin-ovl to work around issue with a bad  
# rpmdb checksum  
# Install xxd and attr utilities  
# Install CONFIG_STACK_VALIDATION dependencies  
RUN yum install -y yum-plugin-ovl vim-common attr libffi libffi-devel \  
elfutils-libelf-devel gcc gcc-c++ python-devel freetype-devel \  
libpng-devel dracut-network nfs-utils trousers-devel libtool && \  
yum clean all && \  
rm -rf /var/cache/yum/* /tmp/* /var/tmp/*  
  
RUN pip install xattr matplotlib requests behave pyhamcrest  
  
COPY dracut.conf /etc/dracut.conf  
  
RUN curl -sSfL
https://github.com/01org/tpm2-tss/releases/download/1.2.0/tpm2-tss-1.2.0.tar.gz
> tpm2-tss-1.2.0.tar.gz && \  
tar -zxf tpm2-tss-1.2.0.tar.gz && \  
cd tpm2-tss-1.2.0 && \  
./configure --prefix=/usr && \  
make && \  
make install && \  
cd .. && \  
rm -rf tpm2-tss-1.2.0 && \  
rm -rf tpm2-tss-1.2.0.tar.gz && \  
ldconfig  
  
# Install EPEL  
RUN yum install -y epel-release && \  
yum clean all && \  
rm -rf /var/cache/yum/* /tmp/* /var/tmp/*  
  
# Install Xen build dependencies  
RUN yum install -y libidn-devel zlib-devel SDL-devel curl-devel \  
libX11-devel ncurses-devel gtk2-devel libaio-devel dev86 iasl \  
gettext gnutls-devel openssl-devel pciutils-devel libuuid-devel \  
bzip2-devel xz-devel e2fsprogs-devel yajl-devel mingw64-binutils \  
systemd-devel glibc-devel.i686 texinfo \  
&& \  
yum clean all && \  
rm -rf /var/cache/yum/* /tmp/* /var/tmp/*  
  
# Install checkpolicy for XSM Xen  
RUN yum install -y checkpolicy \  
&& \  
yum clean all && \  
rm -rf /var/cache/yum/* /tmp/* /var/tmp/*  
  
# Install grub2 build dependencies  
RUN yum install -y device-mapper-devel freetype-devel gettext-devel texinfo \  
dejavu-sans-fonts help2man libusb-devel rpm-devel glibc-static.x86_64 \  
glibc-static.i686 autogen \  
&& \  
yum clean all && \  
rm -rf /var/cache/yum/* /tmp/* /var/tmp/*  
  
# Install yum-utils  
RUN yum install -y yum-utils \  
&& \  
yum clean all && \  
rm -rf /var/cache/yum/* /tmp/* /var/tmp/*  
  
COPY build_binutils /tmp  
  
RUN /tmp/build_binutils  

