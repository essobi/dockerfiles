FROM ubuntu:xenial  
  
ARG GIT_URL=https://github.com/overviewer/Minecraft-Overviewer  
ARG GIT_REF=master  
  
ARG MINECRAFT_URL=https://s3.amazonaws.com/Minecraft.Download/versions  
ARG MINECRAFT_VERSION=1.12.2  
ENV
MINECRAFT_DOWNLOAD_URL=${MINECRAFT_URL}/${MINECRAFT_VERSION}/${MINECRAFT_VERSION}.jar  
ENV BUILD_DEPS="build-essential python-dev git"  
ENV RUNTIME_DEPS="python python-imaging python-numpy wget ca-certificates
optipng"  
RUN apt update  
RUN apt-get install -y --no-install-recommends ${BUILD_DEPS} ${RUNTIME_DEPS}  
RUN mkdir /overviewer  
RUN cd /overviewer  
RUN git init  
RUN git remote add origin ${GIT_URL}  
RUN git fetch origin ${GIT_REF}  
RUN git reset --hard FETCH_HEAD  
RUN sed -i 's/\https:\/\/google-maps-icons\\.googlecode\\.com\/files\///g'
overviewer_core/assetmanager.py  
RUN python setup.py install  
RUN apt-get purge -y ${BUILD_DEPS}  
RUN apt-get autoremove -y --purge  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /tmp/*  
RUN rm -rf /usr/share/icons  
RUN rm -rf /usr/share/poppler  
RUN rm -rf /usr/share/mime  
RUN rm -rf /usr/share/GeoIP  
  
RUN useradd --create-home --shell /bin/false \--system --uid 1000 overviewer  
USER overviewer  
  
RUN wget -P ~/.minecraft/versions/${MINECRAFT_VERSION}/
${MINECRAFT_DOWNLOAD_URL}  
  
ENTRYPOINT ["overviewer.py"]

