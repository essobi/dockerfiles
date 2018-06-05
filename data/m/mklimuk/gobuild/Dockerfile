from golang:1.9  
RUN printf '%s\n' 'path-exclude /usr/share/doc/*' 'path-include
/usr/share/doc/*/copyright' 'path-exclude /usr/share/man/*' 'path-exclude
/usr/share/groff/*' 'path-exclude /usr/share/info/*' 'path-exclude
/usr/share/lintian/*' 'path-exclude /usr/share/linda/*' >
/etc/dpkg/dpkg.cfg.d/01_nodoc && \  
echo 'APT::Install-Recommends "0" ; APT::Install-Suggests "0" ;' >>
/etc/apt/apt.conf && export DEBIAN_FRONTEND=noninteractive && apt-get update
&& \  
apt-get install -yq fakeroot build-essential libasound2-dev
libwebkit2gtk-4.0-dev libjavascriptcoregtk-3.0-dev gir1.2-webkit2-4.0
libgtk-3-dev libsoup2.4-dev gir1.2-gtk-3.0 gir1.2-soup-2.4 libgdk-
pixbuf2.0-dev libatk1.0-dev libatk-bridge2.0-dev gir1.2-atk-1.0
gir1.2-gdkpixbuf-2.0 libatspi2.0-dev libglib2.0-dev  
  
ENV PKG_CONFIG_PATH=/usr/lib/x86_64-linux-gnu/pkgconfig  

