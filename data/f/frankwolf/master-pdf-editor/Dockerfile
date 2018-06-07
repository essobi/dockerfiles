  
FROM ubuntu:xenial  
LABEL Maintainer="Frank Wolf <FrankWolf@gmx.de>" \  
Name="Master PDF Editor" \  
Version=4.3.89  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
ca-certificates \  
libqt5svg5 \  
libsane \  
qt5-default \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
ARG VERSION=4.3.89  
# https://code-industry.net/public/master-pdf-editor-${VERSION}_qt5.amd64.deb  
RUN wget http://get.code-industry.net/public/master-pdf-
editor-${VERSION}_qt5.amd64.deb \  
&& dpkg -i master-pdf-editor-${VERSION}_qt5.amd64.deb \  
&& rm master-pdf-editor-${VERSION}_qt5.amd64.deb \  
&& echo 12345678901234567890123456789012 > /etc/machine-id  
  
ARG USER=user  
ARG UID=1000  
ENV USER $USER  
RUN mkdir /home/$USER \  
&& groupadd -r $USER -g $UID \  
&& useradd -u $UID -r -g $USER -d /home/$USER -s /usr/sbin/nologin -c "Docker
image user" \--no-log-init $USER \  
&& chown -R $USER:$USER /home/$USER  
  
WORKDIR /home/$USER  
USER $USER  
VOLUME /data  
WORKDIR /data  
  
CMD ["/opt/master-pdf-editor-4/masterpdfeditor4"]  

