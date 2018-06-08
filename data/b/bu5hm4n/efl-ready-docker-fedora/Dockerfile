FROM fedora  
  
RUN dnf -y install automake bluez-libs-devel bullet-devel ccache check-devel
curl-devel \  
dbus-devel doxygen fontconfig-devel freetype-devel fribidi-devel gcc gcc-c++ \  
gdb gettext-devel giflib-devel glib2-devel gstreamer1-devel
gstreamer1-plugins-base-devel \  
harfbuzz-devel ibus-devel ImageMagick kernel-devel libdrm-devel libinput-devel
\  
libjpeg-turbo-devel libpng-devel mesa-libEGL-devel mesa-libGL-devel mesa-
libGLES-devel \  
libmount-devel libproxy-devel LibRaw-devel librsvg2-devel libsndfile-devel \  
libspectre-devel libtiff-devel libtool libunwind-devel libwebp-devel
libX11-devel \  
libxkbcommon-devel libxkbfile-devel libXcursor-devel libXdamage-devel libXext-
devel \  
libXinerama-devel libXScrnSaver-devel libXtst-devel luajit-devel make \  
mesa-libgbm-devel mesa-libwayland-egl-devel ninja-build openjpeg2-devel \  
openssl-devel pam-devel perf poppler-cpp-devel pulseaudio-libs-devel \  
python3-pip scim-devel systemd-devel texlive-base uuid-devel \  
valgrind-devel wayland-devel wayland-protocols-devel \  
xcb-util-keysyms-devel xorg-x11-server-Xephyr git clang  
  
RUN pip3 install --user meson  
  
RUN git clone http://git.enlightenment.org/core/efl.git  
  

