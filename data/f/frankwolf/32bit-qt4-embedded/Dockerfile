  
FROM frankwolf/32bit-ubuntu:xenial  
MAINTAINER "Frank Wolf <FrankWolf@gmx.de>"  
LABEL Maintainer="Frank Wolf <FrankWolf@gmx.de>" \  
Name="Qt 4 embedded on x86" \  
Version=0.1.0  
  
SHELL ["/usr/bin/linux32", "sh", "-c"]  
  
ARG QT_VERSION=4.8.6  
ARG QT_CONFIGURE_OPTIONS=  
  
COPY qt/ /opt  
WORKDIR /opt  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
ca-certificates \  
build-essential \  
gdbserver \  
liblog4cxx-dev \  
patch \  
qt4-dev-tools \  
wget \  
&& apt-get build-dep -y \  
qt4-x11 \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
RUN export QT_MAJOR_MINOR=$(echo $QT_VERSION | cut -d'.' -f 1,2) \  
&& if $(wget -q -S --spider
https://download.qt.io/archive/qt/${QT_MAJOR_MINOR}/${QT_VERSION}/qt-
everywhere-opensource-src-${QT_VERSION}.tar.gz > /dev/null 2>&1); then \  
wget https://download.qt.io/archive/qt/${QT_MAJOR_MINOR}/${QT_VERSION}/qt-
everywhere-opensource-src-${QT_VERSION}.tar.gz; \  
else \  
wget https://download.qt.io/archive/qt/${QT_MAJOR_MINOR}/qt-everywhere-
opensource-src-${QT_VERSION}.tar.gz; \  
fi \  
&& tar -xzf qt-everywhere-opensource-src-${QT_VERSION}.tar.gz \  
&& rm qt-everywhere-opensource-src-${QT_VERSION}.tar.gz \  
&& chmod +x *.sh \  
&& if [ -x ./qt-everywhere-opensource-src-${QT_VERSION}-apply-patches.sh ];
then \  
./qt-everywhere-opensource-src-${QT_VERSION}-apply-patches.sh; \  
fi \  
&& cd qt-everywhere-opensource-src-${QT_VERSION} \  
&& ../build-qt.sh ${QT_VERSION}  
  
ARG USER=user  
ARG UID=1000  
ARG GID=1000  
ENV USER $USER  
RUN mkdir /home/$USER \  
&& groupadd -r $USER -g $GID \  
&& useradd -u $UID -r -g $USER -d /home/$USER -s /sbin/nologin -c "Docker
User" $USER \  
&& chown -R $USER:$USER /home/$USER  
  
USER $USER  
ENV QVFB=  
VOLUME /data  
WORKDIR /data  
  
CMD ["bash"]  
  
COPY docker-entrypoint.sh /  
COPY docker-entrypoint.d/* /docker-entrypoint.d/  
ENTRYPOINT ["/docker-entrypoint.sh"]  

