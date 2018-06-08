# https://wiki.moonshot.ja.net/display/Moonshot/Build+Moonshot+from+Source  
# docker build -t jbasney/moonshot .  
# docker run -it jbasney/moonshot bash  
FROM debian  
MAINTAINER Jim Basney <jbasney@illinois.edu>  
ENV container docker  
RUN apt-get update && apt-get install -y \  
apache2-threaded-dev \  
autoconf \  
automake \  
autopoint \  
autotools-dev \  
build-essential \  
desktop-file-utils \  
doxygen \  
fakeroot \  
git \  
libboost-all-dev \  
libconfuse-dev \  
libcurl4-openssl-dev \  
libdbus-glib-1-dev \  
libevent-dev \  
libgee-dev \  
libgnome-keyring-dev \  
libgtk2.0-dev \  
libkrb5-dev \  
liblog4cpp5-dev \  
liblog4shib-dev \  
libsaml2-dev \  
libsqlite3-dev \  
libtalloc-dev \  
libtool \  
libxerces-c-dev \  
libxml-security-c-dev \  
libxmltooling-dev \  
python \  
valac \  
xmltooling-schemas  
RUN git clone --recursive http://www.project-moonshot.org/git/moonshot.git  
RUN cd moonshot && ./builder --prefix=/opt/moonshot  

