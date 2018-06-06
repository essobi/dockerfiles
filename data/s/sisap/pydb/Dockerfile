# instala connectors per a diferents bases de dades, la majoria del codi és
per Oracle  
FROM python:3.5  
MAINTAINER SISAP <sisap@gencat.cat>  
  
# directori de treball  
WORKDIR /build  
  
# variables d'entorn  
ENV ORACLE_HOME /opt/oracle/instantclient_11_2  
ENV LD_LIBRARY_PATH $ORACLE_HOME  
ENV BASEMAP_VERSION 1.0.7  
ENV GEOS_VERSION 3.3.3  
ENV TINI_VERSION 0.14.0  
ENV TINI_PATH /usr/bin/tini  
  
# copiar requirements de context  
COPY requirements.txt .  
  
RUN \  
# update sources  
apt-get update \  
# instalar dependències per instantclient  
&& apt-get install -y \--no-install-recommends \  
libaio-dev \  
unzip \  
# descarregar instantclient (site oficial demana cookies)  
&& curl -JLO https://www.dropbox.com/s/pt6mbhvnyebudoi/instantclient-basic-
linux.x64-11.2.0.4.0.zip?dl=1 \  
&& curl -JLO https://www.dropbox.com/s/uent5o4ochemrnw/instantclient-sdk-
linux.x64-11.2.0.4.0.zip?dl=1 \  
# crear directori i descomprimir instantclient  
&& mkdir -p /opt/oracle \  
&& unzip "instantclient*.zip" -d /opt/oracle \  
# symlink  
&& ln -s $ORACLE_HOME/libclntsh.so.11.2 $ORACLE_HOME/libclntsh.so \  
# instalar paquets de python  
&& pip install --no-cache-dir -r requirements.txt \  
# basemap  
&& wget https://sourceforge.net/projects/matplotlib/files/matplotlib-
toolkits/basemap-${BASEMAP_VERSION}/basemap-${BASEMAP_VERSION}.tar.gz/download
-O basemap.tar.gz \  
&& tar zxf basemap.tar.gz \  
&& cd basemap-${BASEMAP_VERSION} \  
&& cd geos-${GEOS_VERSION} \  
&& ./configure --prefix=/usr/local \  
&& make; make install \  
&& cd .. \  
&& python setup.py install \  
&& cd .. \  
# tini per executar jupyter  
&& wget
https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini -O
${TINI_PATH} \  
&& chmod +x ${TINI_PATH} \  
# clean  
&& rm -rf \  
/build \  
/var/lib/apt/lists/*  

