FROM coopermaa/buildroot:2015.02  
MAINTAINER Cooper Maa <coopermaa77@gmail.com>  
  
ENV IMG_VERSION 2015.04  
RUN make qemu_x86_64_defconfig  
RUN for CFVAR in \  
BR2_TOOLCHAIN_BUILDROOT_LARGEFILE \  
BR2_TOOLCHAIN_BUILDROOT_INET_IPV6 \  
BR2_TOOLCHAIN_BUILDROOT_INET_RPC \  
BR2_TOOLCHAIN_BUILDROOT_WCHAR \  
BR2_TARGET_ROOTFS_TAR \  
; do sed -i "s/# $CFVAR is not set/$CFVAR=y/" .config; done && \  
sed -i
's/BR2_DEFCONFIG.*/BR2_DEFCONFIG="\$(TOPDIR)\/configs\/my_x86_64_defconfig"/'
.config && \  
sed -i
's/BR2_TARGET_GENERIC_GETTY_PORT.*/BR2_TARGET_GENERIC_GETTY_PORT="ttyS0"/'
.config  
make savedefconfig  
  
# oldconfig: resolve any unresolved symbols in .config  
# olddefconfig: same as oldconfig but update deps and sets new symbols to
their default value  
RUN make olddefconfig  
RUN make

