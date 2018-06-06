FROM openmandriva/cooker  
MAINTAINER Bernhard Rosenkraenzer <bero@linaro.org>  
  
WORKDIR /  
ENV HOSTNAME kernelbuild  
  
RUN useradd -u 1000 -m -g users -G wheel kernelbuild  
# This is the right thing to do. Doing the same thing with sed is a workaround  
# for a breakage in shadow-4.4 in cooker.  
# RUN echo -n root:kernelbuild |chpasswd  
RUN sed -i -e
's,^root.*,root:$6$HCvaWfuvfvhyY6rO$8Xm3LT5uY0hpIFWA7GdehYr7XOj/4icoNUllAFOBgP3ndX8xsnbnur4uJkozTvRqgXIzcJHP6pjpRmkRQyTrT.:16729:0:99999:7:::,'
/etc/shadow  
RUN wget http://people.linaro.org/~bernhard.rosenkranzer/cross-aarch64-linux-
gnu-binutils-2.27.90-1-omv3001.x86_64.rpm  
RUN urpmi --auto --no-verify-rpm --auto-update  
RUN urpmi --auto --no-verify-rpm sudo clang lld make 'pkgconfig(ncursesw)' bc
vim-enhanced git-core cross-aarch64-linux-gnu-
binutils-2.27.90-1-omv3001.x86_64.rpm  
# Unbreak su inside docker  
RUN sed -i -e '/\\*.*nice/d' /etc/security/limits.conf  
# Make sudo passwordless  
RUN sed -i -e 's,^%wheel,#%wheel,;s,^# %wheel,%wheel,' /etc/sudoers  
  
USER kernelbuild  
WORKDIR /home/kernelbuild  
RUN git clone -b android-hikey-linaro-4.9-clang --depth 1 git://android-
git.linaro.org/kernel/hikey-clang.git  
RUN echo 'cat <<EOF' >>.bashrc  
RUN echo 'To build the kernel, use' >>.bashrc  
RUN echo 'cd hikey-clang' >>.bashrc  
RUN echo 'make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- LD=aarch64-linux-
gnu-ld.bfd CC=clang HOSTCC=clang hikey_defconfig' >>.bashrc  
RUN echo 'make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- LD=aarch64-linux-
gnu-ld.bfd CC=clang HOSTCC=clang -j`getconf _NPROCESSORS_ONLN`' >>.bashrc  
RUN echo 'EOF' >>.bashrc  
  
CMD ["/bin/bash", "-l"]  

