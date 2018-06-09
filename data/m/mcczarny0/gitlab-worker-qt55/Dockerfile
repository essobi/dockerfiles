FROM gitlab/gitlab-runner  
  
ENV QMAKE=qmake  
ENV PATH="${PATH}:/opt/qt/5.5/gcc_64/bin/"  
ADD qt-installer-noninteractive.qs .  
  
RUN apt-get update && apt-get install -y \--no-install-recommends libsm6
libice6 libxext6 libxrender1 libfontconfig1 libx11-xcb-dev build-essential
libfontconfig1 libXrender1 libsm6 libfreetype6 libglib2.0-0 \  
&& curl -sSL https://download.qt.io/official_releases/online_installers/qt-
unified-linux-x64-online.run -o qt.run \  
&& chmod +x qt.run \  
&& sync \  
&& ./qt.run --platform minimal --script qt-installer-noninteractive.qs -v \  
&& rm -rf \  
qt.run \  
/var/lib/apt/lists/* \  
/opt/qt/update.rcc \  
/opt/qt/components.xml \  
/opt/qt/InstallationLog.txt \  
/opt/qt/MaintenanceTool* \  
/opt/qt/Tools \  
/opt/qt/Docs \  
/opt/qt/network.xml \  
/opt/qt/Examples  

