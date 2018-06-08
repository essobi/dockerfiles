FROM openms/contrib:qt5-v2.3.1  
WORKDIR /  
RUN git clone https://github.com/OpenMS/OpenMS.git && cd OpenMS && \  
hash=`git log | head -n 1 | cut -f 2 -d ' '` && \  
sed -i "s/OPENMS_GIT_SHA1/\"$hash\"/"
src/openms/source/CONCEPT/VersionInfo.cpp && \  
rm -rf .git/ share/OpenMS/examples/  
RUN mkdir openms-build  
  
WORKDIR /openms-build  
  
# Load the Qt5 environment and configure  
RUN QT_ENV=$(find /opt -name 'qt*-env.sh') && /bin/bash -c "source ${QT_ENV}
&& cmake -DCMAKE_PREFIX_PATH='/contrib-build/;/usr/;/usr/local'
-DBOOST_USE_STATIC=OFF ../OpenMS"  
RUN make OpenMS  
  

