FROM obedmr/latex  
MAINTAINER obed.n.munoz@gmail.com  
  
# Update all  
RUN pacman -Sc --noconfirm  
RUN pacman-key --refresh-keys  
RUN pacman -Syu --noconfirm  
  
# Install TexLive utils  
RUN pacman -Sy --noconfirm python-ply python-jinja python-chardet python-
unidecode texlive-fontsextra lilypond python2-setuptools git  
USER yaourt  
RUN mkdir -p /tmp/yaourt/ ; chown yaourt /tmp/yaourt  
USER yaourt  
RUN cd /tmp/yaourt ; yaourt --getpkgbuild aur/python-argparse ; cd python-
argparse ; makepkg ; ls -la  
USER root  
RUN pacman -U --noconfirm /tmp/yaourt/python-argparse/python-
argparse*.pkg.tar.xz  
USER yaourt  
RUN cd /tmp/yaourt ; yaourt --getpkgbuild aur/patacrep-git ; cd patacrep-git ;
makepkg ; ls -la  
USER root  
RUN pacman -U --noconfirm /tmp/yaourt/patacrep-git/patacrep-git*.pkg.tar.xz  
  
WORKDIR "/mnt"

