from trzeci/emscripten:sdk-tag-1.37.18-32bit  
  
run apt-get update  
run apt-get install -y wget bzip2 unzip ca-certificates make  
run wget --quiet https://cmake.org/files/v3.9/cmake-3.9.1-Linux-x86_64.sh \  
&& printf "y\nn\n" | sh cmake-3.9.1-Linux-x86_64.sh --prefix=/opt/cmake \  
&& ln -s /opt/cmake/bin/cpack /usr/local/bin/cpack \  
&& cpack --version  
run mkdir /elma2 && mkdir /elma2/dependencies  
  
env BOOST_MINOR_VER 64  
env CEGUI_BRANCH v0-8  
env CEGUI_VERSION 0.8.7  
env GLFW_VERSION 3.2.1  
env EXPAT_VERSION 2.2.0  
env ZLIB_VERSION 1.2.11  
env GLM_VERSION 0.9.7.5  
workdir /elma2  
run wget --quiet
http://downloads.sourceforge.net/project/boost/boost/1.${BOOST_MINOR_VER}.0/boost_1_${BOOST_MINOR_VER}_0.tar.bz2
\  
&& tar xjf boost_1_${BOOST_MINOR_VER}_0.tar.bz2 -C dependencies \  
&& rm boost_1_${BOOST_MINOR_VER}_0.tar.bz2  
  
run wget --quiet https://bitbucket.org/cegui/cegui/get/v0-8-7.tar.bz2 \  
&& tar xjf v0-8-7.tar.bz2 -C dependencies \  
&& rm v0-8-7.tar.bz2  
  
run wget --quiet https://github.com/g-truc/glm/archive/${GLM_VERSION}.tar.gz \  
&& tar xf ${GLM_VERSION}.tar.gz -C dependencies \  
&& rm ${GLM_VERSION}.tar.gz  
  
run wget --quiet https://github.com/cbeck88/empoxy/archive/master.zip \  
&& unzip master.zip -d dependencies \  
&& rm master.zip  
  
run wget --quiet https://github.com/emscripten-
ports/FreeType/archive/version_1.zip \  
&& unzip version_1.zip -d dependencies \  
&& rm version_1.zip  
  
run wget --quiet
http://downloads.sourceforge.net/project/expat/expat/${EXPAT_VERSION}/expat-${EXPAT_VERSION}.tar.bz2
\  
&& tar xjf expat-${EXPAT_VERSION}.tar.bz2 -C dependencies \  
&& rm expat-${EXPAT_VERSION}.tar.bz2  
  
run wget --quiet
http://downloads.sourceforge.net/project/freeimage/Source%20Distribution/3.17.0/FreeImage3170.zip
\  
&& unzip FreeImage3170.zip -d dependencies \  
&& rm FreeImage3170.zip  
  
run wget --quiet
https://github.com/madler/zlib/archive/v${ZLIB_VERSION}.tar.gz \  
&& tar xf v${ZLIB_VERSION}.tar.gz -C dependencies \  
&& rm v${ZLIB_VERSION}.tar.gz  
  
env MINIZIP_COMMIT=7b8e226c491a77360dbbc71c2429470924555a9e  
  
run wget --quiet
https://github.com/nmoinvaz/minizip/archive/${MINIZIP_COMMIT}.zip \  
&& unzip ${MINIZIP_COMMIT}.zip -d dependencies \  
&& rm ${MINIZIP_COMMIT}.zip  
  
env EMSCRIPTEN=/emsdk_portable/emscripten/tag-1.37.18  
env TOOLCHAIN=${EMSCRIPTEN}/cmake/Modules/Platform/Emscripten.cmake  
env PATH=${PATH}:${EMSCRIPTEN}  
run sed -i 's/-O2/-O3/' ${TOOLCHAIN}  
  
workdir /elma2/dependencies/zlib-${ZLIB_VERSION}  
run emcmake cmake \  
-DCMAKE_BUILD_TYPE=Release -DOFF64_T_run_result=4 -DOFF64_T_run_result__TRYRUN_OUTPUT="" \  
-DCMAKE_INSTALL_PREFIX=${EMSCRIPTEN}/system .  
run make VERBOSE=1 && make install  
  
workdir /elma2/dependencies/minizip-${MINIZIP_COMMIT}  
run emcmake cmake \  
-DCMAKE_PREFIX_PATH=${EMSCRIPTEN}/system \  
-DCMAKE_BUILD_TYPE=Release \  
-DCMAKE_INSTALL_PREFIX=${EMSCRIPTEN}/system .  
run make VERBOSE=1 && make install  
  
workdir /elma2/dependencies/boost_1_${BOOST_MINOR_VER}_0  
run apt-get install -y gcc \  
&& ./bootstrap.sh --with-
libraries=system,filesystem,serialization,signals,thread,date_time,chrono,test,log
\  
&& apt-get -y --purge remove gcc \  
&& apt-get -y clean \  
&& apt-get -y autoclean \  
&& apt-get -y autoremove  
run echo "using gcc : : em++ ;" > /root/user-config.jam  
run sed -i 's/\$(archiver\\[1\\])/emar/'
/elma2/dependencies/boost_1_${BOOST_MINOR_VER}_0/tools/build/src/tools/gcc.jam  
run sed -i 's/\$(ranlib\\[1\\])/emranlib/'
/elma2/dependencies/boost_1_${BOOST_MINOR_VER}_0/tools/build/src/tools/gcc.jam  
run ./b2 install variant=release link=static -j2 --prefix=${EMSCRIPTEN}/system
-d+2  
  
workdir /elma2/dependencies/FreeImage  
run /bin/bash -c 'echo -e "#include <sys/types.h>\n#include <unistd.h>"' >>
Source/ZLib/gzguts.h  
run echo "U32 _byteswap_ulong(U32 bits);" >>
Source/LibJXR/image/sys/strcodec.h  
run echo "#include <wchar.h>" >> Source/LibJXR/jxrgluelib/JXRGlue.h  
run sed -i 's/main/not_main/' Source/OpenEXR/IlmImf/b44ExpLogTable.cpp  
run sed -i 's/?= -O3/= -O3/' Makefile.gnu  
run emmake make VERBOSE=1 -j2  
run emmake make INCDIR=${EMSCRIPTEN}/system/include
INSTALLDIR=${EMSCRIPTEN}/system/lib install  
  
workdir /elma2/dependencies/expat-${EXPAT_VERSION}  
run emcmake cmake \  
-DCMAKE_BUILD_TYPE=Release \  
-DBUILD_tools=OFF -DBUILD_tests=OFF -DBUILD_examples=OFF \  
-DCMAKE_INSTALL_PREFIX=${EMSCRIPTEN}/system .  
run make VERBOSE=1 && make install  
  
workdir /elma2/dependencies/glm-${GLM_VERSION}  
run emcmake cmake \  
-DCMAKE_INSTALL_INCLUDEDIR=${EMSCRIPTEN}/system/include .  
run make && make install  
  
workdir /elma2/dependencies/empoxy-master  
run emcmake cmake \  
-DCMAKE_BUILD_TYPE=Release \  
-DCMAKE_INSTALL_PREFIX=${EMSCRIPTEN}/system .  
run make VERBOSE=1 -j2 && make install  
  
workdir /elma2/dependencies/FreeType-version_1  
run mkdir build && cd build && emcmake cmake \  
-DCMAKE_BUILD_TYPE=Release \  
-DCMAKE_INSTALL_PREFIX=${EMSCRIPTEN}/system ..  
run cd build && make VERBOSE=1 -j2 && make install  
  
workdir /elma2  
run mv dependencies/cegui-cegui-*/ dependencies/cegui-${CEGUI_VERSION}/  
run mkdir dependencies/cegui-${CEGUI_VERSION}/build  
workdir /elma2/dependencies/cegui-${CEGUI_VERSION}/build  
run sed -i 's/FREETYPE FREETYPE_LIB/FREETYPE/' ../cmake/FindFreetype.cmake  
run sed -i 's/EPOXY DEFAULT_MSG EPOXY_LIB EPOXY_H_PATH/EPOXY DEFAULT_MSG
EPOXY_H_PATH/' ../cmake/FindEpoxy.cmake  
run sed \  
-i 's/OPENGLES DEFAULT_MSG OPENGLES_LIB OPENGLES_H_PATH/OPENGLES DEFAULT_MSG OPENGLES_H_PATH/' \  
../cmake/FindOpenGLES.cmake  
run sed -i 's/__linux__/EMSCRIPTEN/' ../cegui/src/SimpleTimer.cpp  
run sed -i 's/__linux__/EMSCRIPTEN/' ../cegui/src/DynamicModule.cpp  
run mv ../cegui/src/falagard/XMLHandler.cpp
../cegui/src/falagard/Falagard_xmlHandler.cpp  
  
run emcmake cmake \  
-DCMAKE_BUILD_TYPE=Release \  
-DCMAKE_INSTALL_PREFIX=${EMSCRIPTEN}/system \  
-DCEGUI_BUILD_STATIC_CONFIGURATION=1 \  
-DCEGUI_BUILD_STATIC_FACTORY_MODULE=1 \  
-DCEGUI_USE_GLEW=0 \  
-DCEGUI_USE_EPOXY=1 \  
-DCEGUI_BUILD_PYTHON_MODULES=0 -DCEGUI_BUILD_IMAGECODEC_FREEIMAGE=1 \  
-DCEGUI_HAS_DEFAULT_LOGGER=0 -DCEGUI_BUILD_IMAGECODEC_TGA=0 \  
-DCEGUI_BUILD_IMAGECODEC_STB=0 -DCEGUI_HAS_PCRE_REGEX=0 \  
-DCEGUI_BUILD_RENDERER_NULL=0 -DCEGUI_BUILD_RENDERER_OPENGLES=0 \  
-DCEGUI_BUILD_RENDERER_OPENGL=0 -DCEGUI_BUILD_RENDERER_OPENGL3=1 \  
-DCEGUI_OPTION_DEFAULT_XMLPARSER="ExpatParser" -DCEGUI_BUILD_XMLPARSER_EXPAT=1 ..  
run make VERBOSE=1 -j2 && make install  
  
# output HTML + JS files for executables instead of only JS  
run sed -i 's/CMAKE_EXECUTABLE_SUFFIX "\\.js"/CMAKE_EXECUTABLE_SUFFIX
".html"/' ${TOOLCHAIN}  
  
copy patches/emscripten/library_glfw.js ${EMSCRIPTEN}/src/library_glfw.js  
  
add
https://raw.githubusercontent.com/glfw/glfw/${GLFW_VERSION}/include/GLFW/glfw3.h
${EMSCRIPTEN}/system/include/GLFW/glfw3.h  

