FROM cogumbreiro/why3:latest  
  
MAINTAINER Tiago Cogumbreiro  
  
ENV ALT_ERGO_VER=0.99.1 \  
Z3_VER=4.4.0 \  
E_VER=1.8  
ENV USER user  
RUN apt-get update -y && \  
apt-get -y install \  
curl \  
tar \  
python \  
make \  
g++ \  
libgomp1 \  
&& \  
cd /tmp && \  
curl -L https://github.com/Z3Prover/z3/archive/z3-$Z3_VER.tar.gz | tar zx && \  
cd /tmp/z3-z3-$Z3_VER && \  
./configure && \  
cd build && \  
make && \  
make install && \  
rm -rf /tmp/z3-z3-$Z3_VER && \  
cd /tmp && \  
curl -L http://wwwlehre.dhbw-
stuttgart.de/~sschulz/WORK/E_DOWNLOAD/V_$E_VER/E.tgz | tar zx && \  
cd /tmp/E && \  
./configure --prefix=/usr/local && \  
make && \  
make install && \  
rm -rf /tmp/E && \  
curl -L http://alt-ergo.ocamlpro.com/download_manager.php?target=alt-ergo-
static-$ALT_ERGO_VER-x86_64 > /usr/local/bin/alt-ergo && \  
chmod a+x /usr/local/bin/alt-ergo && \  
useradd -ms /bin/bash $USER && \  
mkdir /hj-why3 && \  
chown -R $USER:$USER /hj-why3 && \  
apt-get autoremove -y g++ make python curl && \  
apt-get clean  
  
VOLUME /hj-why3  
USER $USER  
RUN why3 config --detect-provers  
WORKDIR /hj-why3  

