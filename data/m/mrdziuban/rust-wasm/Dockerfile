FROM ubuntu:16.04  
MAINTAINER Matt Dziuban "mrdziuban@gmail.com"  
RUN apt-get update && apt-get install -y curl build-essential python2.7 python
git curl cmake  
RUN cd /usr/local && curl -sL https://s3.amazonaws.com/mozilla-
games/emscripten/releases/emsdk-portable.tar.gz | tar xz  
RUN bash -c ". /usr/local/emsdk_portable/emsdk_env.sh && emsdk update && emsdk
install -j1 sdk-incoming-64bit && emsdk activate sdk-incoming-64bit"  
  
RUN curl https://sh.rustup.rs -sSf | sh -s -- --default-toolchain nightly -y  
  
ENV PATH
/root/.cargo/bin:/usr/local/emsdk_portable:/usr/local/emsdk_portable/clang/fastcomp/build_master_64/bin:/usr/local/emsdk_portable/node/4.1.1_64bit/bin:/usr/local/emsdk_portable/emscripten/master:${PATH}  
ENV EM_CONFIG /root/.emscripten  
ENV EMSCRIPTEN /usr/local/emsdk_portable/emscripten/master  
  
RUN rustup toolchain add nightly  
RUN rustup target add asmjs-unknown-emscripten --toolchain nightly  
RUN rustup target add wasm32-unknown-emscripten --toolchain nightly  
  
RUN apt-get autoclean && apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/local/emsdk_portable/zips /usr/local/emsdk_portable/clang/fastcomp/src  
  
RUN echo 'fn main() { println!("test"); }' > /tmp/test.rs  
RUN /bin/bash -l -c 'rustc --target asmjs-unknown-emscripten /tmp/test.rs -o
/tmp/test.js'  
RUN rm /tmp/test.rs && rm /tmp/test.js  
  
VOLUME ["/source"]  
WORKDIR /source  
  
ENTRYPOINT ["/bin/bash", "-l", "-c"]  
CMD ["cargo build --target=asmjs-unknown-emscripten"]  

