FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND noninteractive  
  
ARG WINE_VERSION=winehq-devel  
ARG PYTHON_VERSION=3.5.4  
ARG PYINSTALLER_VERSION=3.2.1  
# we need wine for this all to work, so we'll use the PPA  
RUN set -x \  
&& dpkg --add-architecture i386 \  
&& apt-get update -qy \  
&& apt-get install --no-install-recommends -qfy software-properties-common
wget apt-transport-https \  
&& wget -nc https://dl.winehq.org/wine-builds/Release.key \  
&& apt-key add Release.key \  
&& apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/ \  
&& apt-get update -qy \  
&& apt-get install -qfy --no-install-recommends winehq-devel winetricks \  
&& apt-get clean  
  
# wine settings  
ENV WINEARCH win32  
ENV WINEDEBUG fixme-all  
ENV WINEPREFIX /wine  
  
# PYPI repository location  
ENV PYPI_URL=https://pypi.python.org/  
# PYPI index location  
ENV PYPI_INDEX_URL=https://pypi.python.org/simple  
  
# install python in wine, using the msi packages to install, extracting  
# the files directly, since installing isn't running correctly.  
#  
RUN set -x \  
&& winetricks win7 \  
&& for msifile in `echo core dev exe launcher lib pip path tcltk tools`; do \  
wget -nv
"https://www.python.org/ftp/python/$PYTHON_VERSION/win32/${msifile}.msi"; \  
wine msiexec /a "${msifile}.msi" /qb TARGETDIR=C:/Python35; \  
rm ${msifile}.msi; \  
done \  
&& cd /wine/drive_c/Python35 \  
&& echo 'wine '\''C:\Python35\python.exe'\'' "$@"' > /usr/bin/python \  
&& echo 'wine '\''C:\Python35\Scripts\easy_install.exe'\'' "$@"' >
/usr/bin/easy_install \  
&& echo 'wine '\''C:\Python35\Scripts\pip.exe'\'' "$@"' > /usr/bin/pip \  
&& echo 'wine '\''C:\Python35\Scripts\pyinstaller.exe'\'' "$@"' >
/usr/bin/pyinstaller \  
&& (pip install -U pip || true) \  
&& echo 'assoc .py=PythonScript' | wine cmd \  
&& echo 'ftype PythonScript=c:\Python35\python.exe "%1" %*' | wine cmd \  
&& while pgrep wineserver >/dev/null; do echo "Waiting for wineserver"; sleep
1; done \  
&& chmod +x /usr/bin/python /usr/bin/easy_install /usr/bin/pip
/usr/bin/pyinstaller \  
&& rm -rf /tmp/.wine-*  
  
# install pyinstaller  
RUN set -x \  
&& /usr/bin/pip install pyinstaller==$PYINSTALLER_VERSION  
# && wget
https://pypi.python.org/packages/fd/82/c8a224a9fed3af696463a7af196a891b7652445e914dc3b85f95d6417d4a/pypiwin32-219-cp35-none-
win_amd64.whl#md5=0e1058e35636d2d44b4fd9a4e6abbc27 \  
# && /usr/bin/pip install pypiwin32-219-cp35-none-win_amd64.whl \  
# put the src folder inside wine  
RUN mkdir /src/ && ln -s /src /wine/drive_c/src  
VOLUME /src/  
WORKDIR /wine/drive_c/src/  
RUN mkdir -p /wine/drive_c/tmp  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT []  

