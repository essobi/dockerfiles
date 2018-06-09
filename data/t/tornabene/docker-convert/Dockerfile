# libreoffice-convert 0.0.1  
FROM ubuntu:trusty  
MAINTAINER Tindaro Tornabene <tindaro.tornabene@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get -y -q install python-software-properties software-properties-
common  
RUN add-apt-repository ppa:webupd8team/java -y  
RUN add-apt-repository ppa:libreoffice/ppa -y  
RUN apt-get update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get -yqq install oracle-java7-installer libfontconfig inetutils-ping
net-tools build-essential git zip bzip2 fontconfig ghostscript graphicsmagick
graphicsmagick-imagemagick-compat checkinstall autoconf automake libtool
libjpeg62 libtiff5 libgs-dev ruby libreoffice libreoffice-writer2xhtml
libreoffice-pdfimport  
RUN update-java-alternatives -s java-7-oracle  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-7-oracle" >> ~/.bashrc  
  
WORKDIR /opt  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV OFFICE_HOME /usr/lib/libreoffice  
RUN echo "OFFICE_HOME $OFFICE_HOME."  
  
EXPOSE 12002

