FROM ubuntu:16.04 as builder  
  
RUN \  
apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -y build-essential \  
automake \  
autoconf \  
libsdl2-dev \  
unzip \  
wget \  
cmake \  
nodejs \  
default-jre-headless \  
git-core \  
libsdl-sound1.2-dev  
  
WORKDIR /tmp/emsdk-portable  
  
RUN \  
wget -O /tmp/emsdk-portable.tar.gz https://s3.amazonaws.com/mozilla-
games/emscripten/releases/emsdk-portable.tar.gz \  
&& tar xvzf /tmp/emsdk-portable.tar.gz -C /tmp \  
&& ./emsdk update \  
&& ./emsdk install latest \  
&& ./emsdk activate latest  
  
WORKDIR /em-dosbox  
  
RUN git clone https://github.com/dreamlayers/em-dosbox.git /em-dosbox  
  
RUN \  
bash -c "source /tmp/emsdk-portable/emsdk_env.sh \  
&& ./autogen.sh \  
&& emconfigure \  
&& emconfigure ./configure --with-sdl2 \  
&& make"  
RUN mkdir /cat  
  
RUN \  
wget http://image.dosgamesarchive.com/games/alleycat.zip -O /cat/alleycat.zip
\  
&& unzip /cat/alleycat.zip -d /cat  
  
COPY dosbox.html /em-dosbox/src/dosbox.html  
  
RUN \  
cd src \  
&& ls -lash /cat \  
&& ./packager.py alleycat /cat ALLEYCAT.EXE  
  
FROM nginx:1.12.1-alpine  
  
COPY \--from=builder /em-dosbox/src/alleycat.data /usr/share/nginx/html/  
COPY \--from=builder /em-dosbox/src/alleycat.html
/usr/share/nginx/html/index.html  
COPY \--from=builder /em-dosbox/src/dosbox.js /usr/share/nginx/html/  
COPY \--from=builder /em-dosbox/src/dosbox.html.mem /usr/share/nginx/html/  
  
EXPOSE 80  

