FROM ubuntu  
MAINTAINER gifnksm (makoto.nksm@gmail.com)  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
cmake \  
curl \  
git-core \  
python \  
  
&& git clone --depth 1 https://github.com/juj/emsdk.git \  
&& EMSCRIPTEN_VERSION=$(tail -1 /emsdk/emscripten-tags.txt) \  
&& /emsdk/emsdk install --build=MinSizeRel latest \  
  
&& apt-get -y --purge remove \  
build-essential \  
cmake \  
curl \  
git-core \  
gcc \  
&& apt-get -y clean \  
&& apt-get -y autoclean \  
&& apt-get -y autoremove \  
  
&& mkdir -p /em \  
&& cp -r /emsdk/clang/e${EMSCRIPTEN_VERSION}_64bit /em/clang \  
&& cp -r /emsdk/node/*_64bit/bin/node /em/ \  
  
&& mkdir -p /em/emscripten \  
&& cp -r /emsdk/emscripten/${EMSCRIPTEN_VERSION}/* /em/emscripten \  
&& rm -rf /em/emscripten/tests /em/emscripten/site \  
  
&& rm -rf /emsdk \  
  
&& find /em -executable -exec chmod og+rx "{}" \; \  
&& find /em -not -executable -exec chmod og+r "{}" \; \  
&& find /em/emscripten/ -maxdepth 1 -executable -type f -name 'em*' -exec ln
-s {} /usr/local/bin/ \; \  
&& ln -s /em/node /usr/local/bin \  
&& groupadd --gid 1000 build \  
&& useradd --uid 1000 --gid 1000 --create-home build  
  
USER build  
  
RUN echo "import os\n\  
import os\n\  
LLVM_ROOT='/em/clang'\n\  
EMSCRIPTEN_NATIVE_OPTIMIZER='/em/clang/optimizer'\n\  
BINARYEN_ROOT='/em/clang/binaryen'\n\  
NODE_JS='/em/node'\n\  
EMSCRIPTEN_ROOT='/em/emscripten'\n\  
SPIDERMONKEY_ENGINE = ''\n\  
V8_ENGINE = ''\n\  
TEMP_DIR = '/tmp'\n\  
COMPILER_ENGINE = NODE_JS\n\  
JS_ENGINES = [NODE_JS]\n\  
" > ~/.emscripten \  
&& embuilder.py build ALL \  
&& rm -rf /tmp/*  
  
ENV EM_CONFIG="/home/build/.emscripten" \  
BINARYEN_ROOT="/em/clang/binaryen" \  
EMSCRIPTEN="/em/emscripten"  
  
RUN emcc --version \  
&& mkdir -p /tmp/emscripten_test && cd /tmp/emscripten_test \  
&& printf '#include <iostream>\nint
main(){std::cout<<"HELLO"<<std::endl;return 0;}' > test.cpp \  
&& em++ -O2 test.cpp -o test.js && node test.js \  
&& em++ test.cpp -o test.js && node test.js \  
&& em++ -O2 test.cpp -o test.js -s BINARYEN=1 \  
&& em++ test.cpp -o test.js -s BINARYEN=1 \  
&& cd / \  
&& rm -rf /tmp/*  
  
VOLUME ["/src"]  
WORKDIR /src  

