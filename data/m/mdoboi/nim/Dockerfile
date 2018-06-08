FROM alpine:3.4  
  
RUN apk update && apk upgrade \  
&& apk add g++ git \  
&& rm -rf /var/cache/apk/* \  
&& apk add \--no-cache --virtual=build-dependencies ca-certificates  
  
ENV NIM_VERSION="v0.13.0"  
  
RUN mkdir -p "/opt" \  
&& cd /opt \  
&& git clone -b $NIM_VERSION --depth 1 https://github.com/nim-lang/nim Nim \  
&& cd Nim \  
&& git clone -b $NIM_VERSION --depth 1 https://github.com/nim-lang/csources
csources \  
&& cd csources \  
&& sh build.sh \  
&& cd .. \  
&& rm -rf "./csources" "./tests" \  
&& bin/nim c koch \  
&& ./koch boot -d:release \  
&& ln -s "/opt/Nim/bin/nim" "/usr/local/bin/nim"  
  
RUN cd /opt/Nim \  
&& nim e install_nimble.nims \  
&& ln -s /opt/Nim/bin/nimble /usr/local/bin/nimble  

