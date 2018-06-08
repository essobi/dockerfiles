FROM ubuntu:xenial  
  
ARG GIT_URL=https://github.com/overviewer/Minecraft-Overviewer  
ARG GIT_REF=master  
  
ARG MINECRAFT_URL=https://s3.amazonaws.com/Minecraft.Download/versions  
ARG MINECRAFT_VERSION=1.11.2  
ENV
MINECRAFT_DOWNLOAD_URL=${MINECRAFT_URL}/${MINECRAFT_VERSION}/${MINECRAFT_VERSION}.jar  
ENV BUILD_DEPS="build-essential python-dev git"  
ENV RUNTIME_DEPS="python python-imaging python-numpy wget ca-certificates
optipng"  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ${BUILD_DEPS} ${RUNTIME_DEPS} \  
&& mkdir /overviewer \  
&& cd /overviewer \  
&& git init \  
&& git remote add origin ${GIT_URL} \  
&& git fetch origin ${GIT_REF} \  
&& git reset --hard FETCH_HEAD \  
&& sed -i 's/\https:\/\/google-maps-icons\\.googlecode\\.com\/files\///g'
overviewer_core/assetmanager.py  
&& python setup.py install \  
&& apt-get purge -y ${BUILD_DEPS} \  
&& apt-get autoremove -y --purge \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
&& rm -rf /usr/share/icons \  
&& rm -rf /usr/share/poppler \  
&& rm -rf /usr/share/mime \  
&& rm -rf /usr/share/GeoIP  
  
RUN useradd --create-home --shell /bin/false \--system --uid 1000 overviewer  
USER overviewer  
  
RUN wget -P ~/.minecraft/versions/${MINECRAFT_VERSION}/
${MINECRAFT_DOWNLOAD_URL}  
  
ENTRYPOINT ["overviewer.py"]  

