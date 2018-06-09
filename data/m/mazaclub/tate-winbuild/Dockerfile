FROM ubuntu:14.04  
MAINTAINER Rob Nelson <guruvan@maza.club>  
  
VOLUME ["/opt/wine-electrum/drive_c/tate"]  
#########################  
###  
## git tate [release tag]  
## apt-get install anything than make_packages wants installed to "the host"
(the docker container)  
## pip install anything that the later build or make_packages wants instaleld
to "the host"  
## cd tate  
## make_packages  
## cp package.zip to source/pacakage.zip  
## continue as below  
##  
RUN apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y git python-pip pyqt4-dev-tools zip unzip \  
&& pip install --pre slowaes && pip install ecdsa \  
&& pip install pyasn1 && pip install pyasn1_modules \  
&& pip install qrcode && pip install requests \  
&& pip install tlslite && pip install pbkdf2 \  
&& pip install SocksiPy-branch \  
&& apt-get install -y software-properties-common && add-apt-repository -y
ppa:ubuntu-wine/ppa \  
&& dpkg --add-architecture i386 \  
&& apt-get update -y \  
&& apt-get install -y curl wine1.7 xvfb wget \  
&& apt-get install -y winbind \  
&& apt-get install -y python-pip pyqt4-dev-tools \  
&& apt-get purge -y python-software-properties \  
&& apt-get autoclean -y  
  
# Versions  
ENV PYTHON_URL https://www.python.org/ftp/python/2.7.8/python-2.7.8.msi  
ENV PYQT4_URL
http://downloads.sourceforge.net/project/pyqt/PyQt4/PyQt-4.11.1/PyQt4-4.11.1-gpl-
Py2.7-Qt4.8.6-x32.exe?r=http%3A%2F%2Fwww.riverbankcomputing.co.uk%2Fsoftware%2Fpyqt%2Fdownload&ts=1410031650&use_mirror=skylink  
ENV PYWIN32_URL
http://downloads.sourceforge.net/project/pywin32/pywin32/Build%20217/pywin32-217.win32-py2.7.exe?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fpywin32%2Ffiles%2Fpywin32%2FBuild%2520217%2F&ts=1410031204&use_mirror=kent  
ENV PYINSTALLER_URL
https://pypi.python.org/packages/source/P/PyInstaller/PyInstaller-2.1.zip  
ENV NSIS_URL
http://prdownloads.sourceforge.net/nsis/nsis-2.46-setup.exe?download  
  
# Paths  
ENV WINEPREFIX /opt/wine-electrum  
RUN export WINEPREFIX=/opt/wine-electrum  
  
ENV ELECTRUM_PATH $WINE_PREFIX/drive_c/tate  
ENV PYHOME c:/Python27  
ENV PYTHON xvfb-run -a wine $PYHOME/python.exe -B  
ENV PIP $PYTHON -m pip  
  
# Only needed for debugging  
# RUN apt-get install -y vnc4server  
# RUN export DISPLAY=:33  
# RUN (echo electrum;echo electrum)|vnc4passwd  
# EXPOSE 5933  
# Docker kills this run before wine is done setting up, don't remove the sleep  
RUN xvfb-run -a --server-num=4 wineboot && sleep 5 \  
&& echo 'DIRECTORY IS ' ; pwd \  
&& wget -O python.msi "$PYTHON_URL" \  
&& xvfb-run -a -e /dev/stdout -a msiexec /q /i python.msi \  
&& sleep 5 \  
&& wget -O pyinstaller.zip "$PYINSTALLER_URL" && unzip pyinstaller.zip && mv
PyInstaller-2.1 $WINEPREFIX/drive_c/pyinstaller \  
&& wget -O pywin32.exe "$PYWIN32_URL" \  
&& unzip -qq pywin32.exe; echo 'Done pywin' \  
&& cp -r PLATLIB/* $WINEPREFIX/drive_c/Python27/Lib/site-packages/ \  
&& mkdir -p $WINEPREFIX/drive_c/Python27/Scripts/ \  
&& cp -r SCRIPTS/* $WINEPREFIX/drive_c/Python27/Scripts/ \  
&& $PYTHON $PYHOME/Scripts/pywin32_postinstall.py -install \  
&& wget -O PyQt.exe "$PYQT4_URL" \  
&& rm -rf /tmp/.wine-* && xvfb-run -a wine PyQt.exe /S \  
&& wget -q -O nsis.exe $NSIS_URL \  
&& rm -rf /tmp/.wine-* && xvfb-run -a wine nsis.exe /S  
  
# Pip not needed for releases  
#RUN wget -q -O - https://raw.github.com/pypa/pip/master/contrib/get-pip.py |
$PYTHON  
COPY ./helpers/make_packages /root/make_packages  
COPY ./helpers/make_release /root/make_release  
COPY ./helpers/build-binary /usr/bin/build-binary  
  
# Clean up stale wine processes  
RUN rm -rf /tmp/.wine-*  
## Make package  
#RUN mkdir -p $ELECTRUM_PATH \  
# && echo 'WINEPREFIX -------------' && ls $WINEPREFIX/drive_c/tate \  
# && echo '--------' \  
## && echo 'electrum path ls'  
## && $ELECTRUM_PATH/make_packages  
# && pyrcc4 $ELECTRUM_PATH/icons.qrc -o $ELECTRUM_PATH/gui/qt/icons_rc.py \  
# && pip install --no-compile -t $ELECTRUM_PATH ecdsa \  
# && pip install --no-compile -t $ELECTRUM_PATH pyasn1 \  
# && pip install --no-compile -t $ELECTRUM_PATH pyasn1_modules \  
# && pip install --no-compile -t $ELECTRUM_PATH qrcode \  
# && pip install --no-compile -t $ELECTRUM_PATH requests \  
# && pip install --no-compile -t $ELECTRUM_PATH tlslite \  
# && pip install --pre --no-compile -t $ELECTRUM_PATH/lib slowaes \  
# && pip install --no-compile -t $ELECTRUM_PATH/lib pbkdf2 \  
# && pip install --no-compile -t $ELECTRUM_PATH/lib SocksiPy-branch  
# && git clone https://github.com/mazaclub/tate.git \  
# && cd tate && git checkout $MKPKG_VER && cd ..  
#RUN echo 'making packages' && cd tate \  
# && mkdir packages && ./make_packages && cd .. \  
# && cp tate/dist/Tate-$MKPKG_VER.zip /opt/wine-electrum/drive_c/tate \  
# && unzip /opt/wine-electrum/drive_c/tate  

