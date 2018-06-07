FROM brujoand/dockzb  
  
MAINTAINER Anders Brujordet  
  
RUN apk --update add \  
unrar p7zip unzip libxslt && \  
apk --update add --virtual deps \  
linux-headers automake m4 autoconf libsigc++-dev libffi-dev openssl-dev
libxml2-dev libxslt-dev  
  
RUN pip install --upgrade pip && pip install cffi configobj feedparser
pyOpenSSL support pydbus http://www.golug.it/pub/yenc/yenc-0.4.0.tar.gz  
  
RUN mkdir /build && cd /build && \  
wget https://launchpad.net/libpar2/trunk/0.4/+download/libpar2-0.4.tar.gz &&
tar xfz libpar2-0.4.tar.gz && \  
cd libpar2-0.4 && ./configure && make && make install && cd /build && \  
wget
http://sourceforge.net/projects/parchive/files/par2cmdline/0.4/par2cmdline-0.4.tar.gz
&& \  
tar xfz par2cmdline-0.4.tar.gz && cd par2cmdline-0.4 && \  
sed 's/^bool ReedSolomon/template <> bool ReedSolomon/' reedsolomon.cpp >
reedsolomon.cpp.fixed && mv reedsolomon.cpp.fixed reedsolomon.cpp && \  
aclocal && automake --add-missing && autoconf && ./configure && make && make
install && \  
cd / && rm -rf /build && apk del deps && rm -rf /var/cache/apk/*  
  
RUN git clone -b master --single-branch https://github.com/sabnzbd/sabnzbd
/opt/sabnzbd  
  
EXPOSE 8080  
ENTRYPOINT [ "./safe_run.sh", "python", "/opt/sabnzbd/SABnzbd.py", "--config-
file", "/config/sabnzbd/sabnzbd.ini", "--console", "-s", "0.0.0.0:8080", "-b",
"0" ]  

