FROM opensuse:42.2  
MAINTAINER github/pontostroy  
  
RUN zypper --gpg-auto-import-keys ar -f
http://download.opensuse.org/repositories/home:/pontostroy:/X11/openSUSE_Leap_42.2/
pont; \  
zypper mr -p 20 pont; \  
zypper --gpg-auto-import-keys ar -f
http://download.opensuse.org/repositories/home:/mnhauke:/opencl:/stable/openSUSE_Leap_42.2/
opencl; \  
zypper --gpg-auto-import-keys ar -f
http://download.opensuse.org/repositories/games:/tools/openSUSE_Leap_42.2/
games-tools; \  
zypper --gpg-auto-import-keys ar -f
http://download.opensuse.org/repositories/games/openSUSE_Leap_42.2/ games; \  
zypper --gpg-auto-import-keys ar -f
http://download.opensuse.org/repositories/multimedia:/libs/openSUSE_Leap_42.2/
media_libs; \  
zypper --gpg-auto-import-keys ar -f
http://download.opensuse.org/repositories/security/openSUSE_Leap_42.2/
security; \  
zypper --gpg-auto-import-keys ar -f
http://download.opensuse.org/repositories/home:/pontostroy:/gst/openSUSE_Leap_42.2/
pont_gst;\  
zypper mr -p 15 pont_gst; \  
zypper --gpg-auto-import-keys ar -f
http://ftp.gwdg.de/pub/linux/misc/packman/suse/openSUSE_Leap_42.2/ packman;\  
zypper --gpg-auto-import-keys ref -s; \  
zypper -n in \--force-resolution krb5; \  
zypper -n up --gpg-auto-import-keys --force-resolution; \  
zypper -n in \--no-recommends -l --replacefiles --force-resolution Mesa Mesa-
demos libtxc_dxtn Mesa-libGL1 Mesa-libd3d Mesa-libGLESv2-2 \  
Mesa-libglapi0 bash libXpm4 libasound2 libvulkan1 libvulkan_radeon
libvulkan_intel vulkan libassimp3 xorg-x11-server-wayland \  
Mesa-libGLESv1_CM1 libgbm1 libGLU1 libGLEW1_13 pciutils mc less \  
llvm-r600-clang libgomp1 libfreeimage3 libglut3 libgobject-2_0-0
libgthread-2_0-0 htop \  
libX11-xcb1 libxcb1 libxcb-glx0 libxcb-present0 libXi6 libICE6 libSM6 libXtst6
libXinerama1 \  
libxcb-xinerama0 libfreetype6 fontconfig glibc-locale fonts-config libmad0 \  
dejavu-fonts bitstream-vera php5 php5-zip php5-bz2 php5-gd php5-mbstring \  
php5-ctype php5-xmlreader php5-gettext php5-zlib php5-dom php5-pcntl
php5-posix php5-curl php5-json php5-openssl librtmp1 xrandr gwenhywfar-tools \  
libxcb-xf86dri0 libxcb-xv0 libxcb-util1 libxcb-image0 libxcb-dpms0 libxcb-
dpms0 libxcb-cursor0 libxcb-damage0 libxcb-render-util0 libopusfile0
libmikmod3 \  
libxcb-composite0 libXTrap6 libXfont1 libXft2 libXss1 \  
libSDL-1_2-0 libSDL2-2_0-0 libSDL_gfx15 libSDL2_gfx-1_0-0 curl wget
libgcrypt11 \  
libSDL2_image-2_0-0 libSDL2_mixer-2_0-0 sudo libstdc++6 libgnutls-openssl27
alsa-plugins-pulse alsa-oss \  
libcrypto38 libssl39 libtls11 libalut0 libphysfs1 libspeexdsp1 libspeex1 alsa
alsa-utils apulse strace which \  
wine steam tar unzip coreutils ca-certificates-cacert ca-certificates-mozilla
libcanberra-gtk2-module \  
Mesa-libd3d-32bit Mesa-libGLESv1_CM1-32bit Mesa-libGLESv2-2-32bit
libbz2-1-32bit libGLEW1_13-32bit libXi6 libICE6-32bit libSM6-32bit
libXss1-32bit libXtst6-32bit libXinerama1-32bit libtxc_dxtn-32bit \  
libSDL-1_2-0-32bit libSDL2-2_0-0-32bit libSDL_gfx15-32bit
libSDL2_gfx-1_0-0-32bit libusb-1_0-0-32bit \  
libcrypto38-32bit libssl39-32bit libtls11-32bit libgbm1-32bit libGLU1-32bit
gconf2-32bit alsa-plugins-pulse-32bit alsa-oss-32bit \  
libxcb-xf86dri0-32bit libxcb-xv0-32bit libxcb-util1-32bit libxcb-image0-32bit
libxcb-dpms0-32bit libxcb-dpms0-32bit libxcb-cursor0-32bit \  
libxcb-damage0-32bit libxcb-render-util0-32bit libXft2-32bit \  
libxcb-composite0-32bit libXTrap6-32bit libXfont1-32bit \  
mpv gst-omx gstreamer gstreamer-plugins-bad gstreamer-plugins-base gstreamer-
plugins-good gstreamer-plugins-ugly gstreamer-plugins-vaapi vaapi-intel-driver
Mesa-libva libvdpau_radeonsi \  
libvdpau_r600 libvdpau_nouveau libomx_mesa vaapi-tools libomxil-bellagio
gstreamer-utils xwininfo weston libglfw3 libglfw2 fetchmsttfonts
libvirglrenderer0 Mesa-libOpenCL Mesa-libOpenCL-32bit clinfo libOpenCL1;\  
zypper clean  
  
RUN /usr/sbin/fonts-config; \  
ln -s /sbin/lspci /usr/bin/lspci; \  
ln -s /usr/lib64/libGLEW.so.1.13 /usr/lib64/libGLEW.so.1.5; \  
ln -s /usr/lib64/libudev.so.1 /usr/lib64/libudev.so.0; \  
ln -s /usr/lib64/libbz2.so.1 /usr/lib64/libbz2.so.1.0; \  
ln -s /usr/lib/libGLEW.so.1.13 /usr/lib/libGLEW.so.1.5; \  
ln -s /usr/lib/libudev.so.1 /usr/lib/libudev.so.0; \  
ln -s /usr/lib/libbz2.so.1 /usr/lib/libbz2.so.1.0; \  
ln -s /usr/lib64/librtmp.so.1 /usr/lib64/librtmp.so.0; \  
ln -s /usr/share/gwenhywfar/ca-bundle.crt /etc/ssl/certs/ca-certificates.crt;
\  
ln -s /usr/share/gwenhywfar/ca-bundle.crt /etc/ssl/certs/ca-bundle.crt; \  
rm -rf /var/log/zypper.log; \  
rm -rf /etc/cron.daily/*; \  
rm -rf /etc/cron.hourly/*; \  
rm -rf /var/log/lastlog; \  
rm -rf /var/log/zypp/*; \  
rm -rf /var/log/pbl.log; \  
rm -rf /usr/share/cracklib; \  
rm -rf /usr/bin/dwp; \  
rm -rf /usr/share/doc; \  
rm -rf /var/share/wine/gecko; \  
rm -rf /var/cache/zypp*; \  
rm -rf /var/cache/zypp*; \  
rpm -qa > /listrpms; \  
date +"%m_%d_%Y" > /gog_version  
  
RUN useradd -g users -d /home/gog -m gog -s /bin/bash -p '*'; \  
usermod -a -G wheel gog; \  
echo "Defaults !insults" > /etc/sudoers; \  
echo "gog ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers; \  
echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers; \  
mkdir -p /home/gog/.local/share/Steam; \  
mkdir /home/gog/.steam; \  
chown -hR gog:users /home/gog; \  
passwd -d root  
  
USER gog  
COPY ./env.sh /home/gog/.bashrc  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/bin/bash","/docker-entrypoint.sh"]  

