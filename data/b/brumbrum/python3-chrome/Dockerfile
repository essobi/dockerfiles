ARG DOCKER_TAG  
FROM brumbrum/python3:$DOCKER_TAG as builder  
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Installo le dipendenze per poter buildare  
RUN \  
dpkg --add-architecture i386 && \  
apt-get -y update && \  
apt-get -y install git build-essential clang curl sudo lsb-release apt-utils
file  
  
# Clono il progetto e ne metto il path in PATH  
ENV DEPOT_TOOLS /usr/bin/depot_tools  
ENV PATH $PATH:$DEPOT_TOOLS  
RUN git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
$DEPOT_TOOLS  
  
# Per un grande repository ci vuole un grande buffer!  
# https://www.youtube.com/watch?v=M58X0xV-zK4  
RUN git config --global https.postBuffer 1048576000  
  
# Download Chromium sources.  
RUN fetch --nohooks --no-history chromium  
  
# Avvio i vari hook sul codice  
WORKDIR /data  
RUN gclient runhooks  
  
# Installo le dipendenze di sistema  
# più un paio di fix perché c'erano problemi nel risolvere dipendenze  
# o errori di installazione nei pacchetti  
# (in futuro si può provare senza le prime due righe)  
WORKDIR src  
RUN \  
mkdir -p /usr/share/man/man1 && \  
apt-get -y install g++-arm-linux-gnueabihf && \  
build/install-build-deps.sh --no-prompt  
  
# Modifico chromium per renderlo difficilmente riconoscibile  
# generando una stringa casuale e sostituendola alla stringa riconoscibile  
# https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-
are-using-selenium-with-chromedriver  
RUN \  
ciao=$(head -200 /dev/urandom | cksum | cut -f1 -d " ") && \  
sed -i -e "s/\$cdc_asdjflasutopfhvcZLmcfl_/ie6_${ciao}_/"
/data/src/chrome/test/chromedriver/js/call_function.js  
  
# Compilo chromedriver  
RUN gn gen out/Release --args="is_debug=false"  
RUN ninja -C out/Release chromedriver  
  
################################################################################  
### Creo il vero container, importando l'eseguibile dalla build precedente
#####  
################################################################################  
ARG DOCKER_TAG  
FROM brumbrum/python3:$DOCKER_TAG  
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>  
  
# Prendo il file compilato nello stage precedente  
COPY \--from=builder /data/src/out/Release/chromedriver /usr/bin/chromedriver  
  
RUN \  
apt-get --no-install-recommends -y install wget curl gnupg && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list && \  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add - && \  
apt-get update && \  
apt-get --no-install-recommends -y install google-chrome-stable && \  
apt-get -y purge curl gnupg && \  
apt-get -y autoclean && \  
apt-get -y clean && \  
apt-get -y autoremove  

