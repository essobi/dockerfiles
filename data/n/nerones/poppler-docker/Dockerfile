FROM debian:jessie-backports  
  
RUN apt-get update && apt-get install -t jessie-backports \  
wget \  
build-essential \  
pkg-config \  
libfontconfig1-dev \  
cmake \  
libopenjpeg-dev \  
libjpeg-dev \  
libopenjp2-7-dev \  
libnss3-dev \  
libnss3-tools \  
unzip -y  
RUN wget https://github.com/nerones/poppler/archive/experimental.zip  
RUN unzip experimental.zip \  
&& cd poppler-experimental \  
&& mkdir build && cd build && cmake .. -DCMAKE_INSTALL_PREFIX=/usr
-DCMAKE_BUILD_TYPE=release \  
&& make && make install \  
&& mkdir $HOME/.mozilla/firefox -p \  
&& mkdir /etc/pki/nssdb -p \  
COPY pass .  
COPY ACRaíz.crt .  
COPY AutoridadCertificantedeFirmaDigital.crt .  
RUN certutil -N -d sql:/etc/pki/nssdb -f pass \  
&& certutil -A -t "C,C,CT" -d sql:/etc/pki/nssdb -n 'Root Arg' -i ACRaíz.crt
-f pass \  
&& certutil -A -t "C,C,CT" -d sql:/etc/pki/nssdb -n 'AC onti' -i
AutoridadCertificantedeFirmaDigital.crt -f pass  

