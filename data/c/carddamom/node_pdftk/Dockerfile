FROM node:alpine  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/opt/calibre/lib  
ENV PATH $PATH:/opt/calibre/bin  
ENV CALIBRE_INSTALLER_SOURCE_CODE_URL
https://raw.githubusercontent.com/kovidgoyal/calibre/master/setup/linux-
installer.py  
RUN apk add --update --no-cache \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing \  
alpine-sdk \  
vips-dev \  
fftw-dev \  
python \  
pdftk \  
ocaml \  
libelf-dev \  
git \  
openssh-client \  
tar \  
libarchive \  
gzip \  
bzip2 \  
cpio \  
ca-certificates \  
openssl \  
bash \  
gcc \  
mesa-gl \  
qt5-qtbase-x11 \  
wget \  
xdg-utils \  
xz && \  
wget -O- ${CALIBRE_INSTALLER_SOURCE_CODE_URL} | python -c "import sys;
main=lambda:sys.stderr.write('Download failed\n'); exec(sys.stdin.read());
main(install_dir='/opt', isolated=True)" && \  
rm -rf /tmp/calibre-installer-cache  

