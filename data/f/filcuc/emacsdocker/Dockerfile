FROM debian:jessie  
MAINTAINER Filippo Cucchetto  
RUN apt-get update  
RUN apt-get install -y git build-essential emacs-nox python curl cmake libssl-
dev  
WORKDIR /temp  
  
# install rust  
RUN curl -O https://static.rust-lang.org/dist/rust-1.3.0-x86_64-unknown-linux-
gnu.tar.gz && \  
tar xf *.gz && \  
rm *.gz && \  
./rust*/install.sh --prefix=/opt/rust && \  
rm -rf *  
  
# install rust sources  
RUN curl -O https://static.rust-lang.org/dist/rustc-1.3.0-src.tar.gz && \  
tar xf *.gz && \  
rm *.gz && \  
mv rust*/src /opt/rust && \  
rm -rf *  
  
# add rust to path  
ENV PATH=/opt/rust/bin:$PATH \  
LD_LIBRARY_PATH=/opt/rust/lib:$LD_LIBRARY_PATH \  
RUST_SRC_PATH=/opt/rust/src  
  
# install racer  
WORKDIR /opt  
RUN git clone https://github.com/phildawes/racer.git && \  
cd racer && \  
cargo build --release  
  
# add racer to path  
ENV PATH /opt/racer/target/release:$PATH  
  
# install nim  
RUN git clone https://github.com/nim-lang/Nim.git && \  
cd Nim && \  
git clone \--depth 1 git://github.com/nim-lang/csources && \  
cd csources && sh build.sh && \  
cd .. && \  
bin/nim c koch && \  
./koch boot -d:release && \  
chmod a+rx bin/* && \  
cd .. && \  
chown -R root:users Nim  
  
# add nim to path  
ENV PATH /opt/Nim/bin:$PATH  
  
# install nimble  
RUN cd /opt/Nim && \  
nim install_nimble.nims  
  
# install nimsuggest  
RUN git clone https://github.com/nim-lang/nimsuggest.git && \  
cd nimsuggest && \  
nimble build -y  
  
# add nimsuggest to path  
ENV PATH /opt/nimsuggest:$PATH  
  
# Add emacs user  
RUN useradd -ms /bin/bash emacs  
USER emacs  
WORKDIR /home/emacs  
# Add paths  
ENV PATH=/opt/rust/bin:/opt/racer/target/release:/opt/Nim/bin:$PATH \  
LD_LIBRARY_PATH=/opt/rust/lib:$LD_LIBRARY_PATH \  
RUST_SRC_PATH=/opt/rust/src \  
  
# sets the entry point  
#ENTRYPOINT /bin/bash  

