FROM ubuntu:trusty  
  
LABEL maintainer "vera@genomics.fsu.edu"  
  
VOLUME ["/data"]  
  
ENV URL https://mirror.oxfordnanoportal.com/software/metrichor-agent/epi2me-
agent-2.46.409983.deb  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y \  
fontconfig \  
fontconfig-config \  
fonts-dejavu-core \  
gconf-service \  
gconf-service-backend \  
gconf2-common \  
hicolor-icon-theme \  
krb5-locales \  
libasn1-8-heimdal \  
libatk1.0-0 \  
libatk1.0-data \  
libavahi-client3 \  
libavahi-common-data \  
libavahi-common3 \  
libcairo2 \  
libcups2 \  
libdatrie1 \  
libdbus-glib-1-2 \  
libfontconfig1 \  
libfreetype6 \  
libgconf-2-4 \  
libgconf2-4 \  
libgdk-pixbuf2.0-0 \  
libgdk-pixbuf2.0-common \  
libglib2.0-0 \  
libglib2.0-data \  
libgraphite2-3 \  
libgssapi-krb5-2 \  
libgssapi3-heimdal \  
libgtk2.0-0 \  
libgtk2.0-bin \  
libgtk2.0-common \  
libharfbuzz0b \  
libhcrypto4-heimdal \  
libheimbase1-heimdal \  
libheimntlm0-heimdal \  
libhx509-5-heimdal \  
libjasper1 \  
libjbig0 \  
libjpeg-turbo8 \  
libjpeg8 \  
libk5crypto3 \  
libkeyutils1 \  
libkrb5-26-heimdal \  
libkrb5-3 \  
libkrb5support0 \  
libldap-2.4-2 \  
libpango-1.0-0 \  
libpangocairo-1.0-0 \  
libpangoft2-1.0-0 \  
libpixman-1-0 \  
libroken18-heimdal \  
libsasl2-2 \  
libsasl2-modules \  
libsasl2-modules-db \  
libthai-data \  
libthai0 \  
libtiff5 \  
libwind0-heimdal \  
libx11-6 \  
libx11-data \  
libx11-xcb1 \  
libxau6 \  
libxcb-render0 \  
libxcb-shm0 \  
libxcb1 \  
libxcomposite1 \  
libxcursor1 \  
libxdamage1 \  
libxdmcp6 \  
libxext6 \  
libxfixes3 \  
libxi6 \  
libxinerama1 \  
libxml2 \  
libxrandr2 \  
libxrender1 \  
libxss1 \  
libxtst6 \  
sgml-base \  
shared-mime-info \  
x11-common \  
xml-core \  
libasound2-dev \  
libnss3-dev \  
wget  
  
WORKDIR /root  
RUN wget $URL  
RUN dpkg -i *.deb  
WORKDIR /data  
  
ENTRYPOINT ["/opt/metrichor/EPI2MEAgent"]  

