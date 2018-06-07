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
  
&& git clone https://github.com/juj/emsdk.git \  
&& /emsdk/emsdk install --build=MinSizeRel sdk-incoming-64bit binaryen-
master-64bit \  
  
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
  
&& cp -r /emsdk/clang/fastcomp/build_incoming_64/bin /em/clang \  
&& cp -r /emsdk/node/*_64bit/bin/node /em/ \  
  
&& mkdir -p /em/emscripten \  
&& cp -r /emsdk/emscripten/incoming/* /em/emscripten \  
&& cp -r /emsdk/emscripten/incoming_64bit_optimizer/optimizer /em/emscripten \  
&& rm -rf /em/emscripten/tests /em/emscripten/site \  
  
&& mkdir -p /em/binaryen \  
&& cp -r /emsdk/binaryen/master_64bit_binaryen/bin /em/binaryen/ \  
&& cp -r /emsdk/binaryen/master_64bit_binaryen/lib /em/binaryen/ \  
  
&& rm -rf /emsdk \  
  
&& find /em/emscripten/ -maxdepth 1 -executable -type f -name 'em*' -exec ln
-s {} /usr/local/bin/ \; \  
&& ln -s /em/node /usr/local/bin  
  
ADD .emscripten /root/.emscripten  
  
RUN embuilder.py build ALL \  
&& rm -rf /tmp/*  
  
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

