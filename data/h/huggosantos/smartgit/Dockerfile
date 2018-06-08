FROM ubuntu:14.04  
MAINTAINER Huggo Santos Oliveira <huggo.oliveira1@gmail.com>  
  
USER root  
  
RUN apt-get update  
RUN apt-get install -y git  
RUN apt-get install -q -y axel  
RUN apt-get clean  
  
RUN axel http://www.syntevo.com/static/smart/download/smartgit/smartgit-
linux-7_1_2.tar.gz  
RUN tar -vzxf smartgit-linux-7_1_2.tar.gz  
  
RUN apt-get install -q -y ca-certificates ca-certificates-java fontconfig-
config fonts-dejavu-core git git-man icedtea-7-jre-jamvm java-common
krb5-locales libasn1-8-heimdal libavahi-client3 libavahi-common-data libavahi-
common3 libcups2 libcurl3-gnutls libedit2 liberror-perl libfontconfig1
libfreetype6 libglib2.0-0 libglib2.0-data libgssapi-krb5-2 libgssapi3-heimdal
libhcrypto4-heimdal libheimbase1-heimdal libheimntlm0-heimdal
libhx509-5-heimdal libidn11 libjpeg-turbo8 libjpeg8 libk5crypto3 libkeyutils1
libkrb5-26-heimdal libkrb5-3 libkrb5support0 liblcms2-2 libldap-2.4-2 libnspr4
libnss3 libnss3-1d libnss3-nssdb libpcsclite1 libroken18-heimdal librtmp0
libsasl2-2 libsasl2-modules libsasl2-modules-db libwind0-heimdal libx11-6
libx11-data libxau6 libxcb1 libxdmcp6 libxext6 libxml2 libxmuu1 openjdk-7-jre-
headless openssh-client openssl patch rsync sgml-base shared-mime-info tzdata-
java xauth xml-core  
  
RUN apt-get install -q -y fontconfig hicolor-icon-theme libatk1.0-0
libatk1.0-data libcairo2 libdatrie1 libgdk-pixbuf2.0-0 libgdk-pixbuf2.0-common
libgraphite2-3 libgtk2.0-0 libgtk2.0-bin libgtk2.0-common libharfbuzz0b
libjasper1 libjbig0 libpango-1.0-0 libpangocairo-1.0-0 libpangoft2-1.0-0
libpixman-1-0 libthai-data libthai0 libtiff5 libxcb-render0 libxcb-shm0
libxcomposite1 libxcursor1 libxdamage1 libxfixes3 libxi6 libxinerama1
libxrandr2 libxrender1 libxtst6 x11-common  
  
CMD /smartgit/bin/smartgit.sh  

