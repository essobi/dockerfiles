FROM ubuntu:16.04  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list \  
&& apt-get update -qq \  
&& apt-get install -qqy curl fontconfig wget cabextract xfonts-utils\  
&& echo "ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
boolean true" \  
| debconf-set-selections \  
&& curl -O "http://ftp.de.debian.org/debian/pool/contrib/m/msttcorefonts/ttf-
mscorefonts-installer_3.6_all.deb" \  
&& dpkg -i ttf-mscorefonts-installer_3.6_all.deb \  
&& rm -rf /var/lib/apt/lists/* ttf-mscorefonts-installer_3.6_all.deb  
  
RUN curl -sLH "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/server-
jre-8u161-linux-x64.tar.gz \  
| tar -xzf - -C /opt \  
&& mv /opt/jdk1.8*/jre /opt/ \  
&& rm -rf /opt/jdk1.8*  
  
ENV INSTALL4J_JAVA_HOME='/opt/jre' \  
LANG='C.UTF-8' \  
LC_ALL='C.UTF-8' \  
LANGUAGE='C.UTF-8'  
ADD ./config /a/config  
  
RUN curl http://static.adito.de/common/install/ADITO4_4.6.151_unix.sh >
/tmp/adito.sh \  
&& chmod u+x /tmp/adito.sh \  
&& /tmp/adito.sh -q -varfile /a/config/response.varfile \  
&& rm -rf /tmp/*  
  
EXPOSE 7934 7779 7778 7733 161/udp 80  
WORKDIR /opt/ADITO4  
  
ADD ./start.sh /a/start.sh  
RUN chmod u+x /a/start.sh  
CMD /a/start.sh  

