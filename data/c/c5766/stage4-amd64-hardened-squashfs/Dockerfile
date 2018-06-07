  
FROM gentoo/stage3-amd64-hardened  
  
RUN emerge-webrsync  
  
RUN eselect profile set hardened/linux/amd64  
  
RUN emerge --update --deep --newuse @world  
  
RUN sed -i 's/#en_US.UTF-8/en_US.UTF-8/' /etc/locale.gen  
  
RUN locale-gen  
  
RUN eselect locale set en_US.utf8  
  
RUN . /etc/profile  
  
RUN echo "sys-kernel/hardened-sources symlink" >>
/etc/portage/package.use/hardened-sources  
  
RUN emerge sys-kernel/hardened-sources  
  
RUN cd /usr/src/linux  
  
# RUN make defconfig  
# RUN make ARCH=x86_64 x86_64_defconfig  
# COPY kernel-configurations/.config.defconfig.netcard.fs
/usr/src/linux/.config  
# RUN make && make modules_install  

