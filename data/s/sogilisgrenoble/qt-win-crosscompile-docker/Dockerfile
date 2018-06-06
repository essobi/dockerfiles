FROM base/archlinux:2018.03.01  
  
# Select a mirror  
RUN cp /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist.backup \  
&& rankmirrors -n 6 /etc/pacman.d/mirrorlist.backup > /etc/pacman.d/mirrorlist  
  
# Update base system  
RUN pacman -Sy --noconfirm --noprogressbar archlinux-keyring \  
&& pacman-key --populate \  
&& pacman -Su --noconfirm --noprogressbar pacman \  
&& pacman-db-upgrade \  
&& pacman -Su --noconfirm --noprogressbar ca-certificates \  
&& trust extract-compat \  
&& pacman -Syyu --noconfirm --noprogressbar \  
&& (echo -e "y\ny\n" | pacman -Scc) \  
# Add mingw-repo  
&& echo "[ownstuff]" >> /etc/pacman.conf \  
&& echo "SigLevel = Optional TrustAll" >> /etc/pacman.conf \  
&& echo "Server = https://martchus.no-ip.biz/repo/arch/ownstuff/os/\$arch" >>
/etc/pacman.conf \  
&& pacman -Sy \  
# Add packages to the base system  
&& pacman -S --noconfirm --noprogressbar \  
python python-pip make \  
&& (echo -e "y\ny\n" | pacman -Scc) \  
&& pacman -S --noconfirm --noprogressbar \  
mingw-w64-binutils \  
mingw-w64-gcc \  
mingw-w64-headers \  
mingw-w64-winpthreads \  
mingw-w64-cmake \  
mingw-w64-freeglut \  
mingw-w64-openssl \  
mingw-w64-pkg-config \  
mingw-w64-qt5-base \  
mingw-w64-qt5-declarative \  
mingw-w64-qt5-graphicaleffects \  
mingw-w64-qt5-imageformats \  
mingw-w64-qt5-location \  
mingw-w64-qt5-multimedia \  
mingw-w64-qt5-quickcontrols \  
mingw-w64-qt5-script \  
mingw-w64-qt5-sensors \  
mingw-w64-qt5-svg \  
mingw-w64-qt5-tools \  
mingw-w64-qt5-translations \  
mingw-w64-qt5-webkit \  
mingw-w64-qt5-websockets \  
mingw-w64-qt5-winextras \  
mingw-w64-boost \  
mingw-w64-qt5-quickcontrols2 \  
mingw-w64-qt5-serialport \  
mingw-w64-configure \  
&& pip install conan \  
&& conan remote add bincrafters
https://api.bintray.com/conan/bincrafters/public-conan \  
&& (echo -e "y\ny\n" | pacman -Scc) \  
&& paccache -r -k0; \  
rm -rf /usr/share/man/*; \  
rm -rf /tmp/*; \  
rm -rf /var/tmp/*  
  
VOLUME /root/.conan  

