FROM dockcross/linux-armv6  
MAINTAINER Erwin Gribnau "erwin@gribnau.org"  
  
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y  
RUN /root/.cargo/bin/rustup target add arm-unknown-linux-gnueabihf  
RUN ln -s /root/.cargo/bin/cargo /usr/local/sbin/cargo && \  
ln -s /root/.cargo/bin/rustc /usr/local/sbin/rustc && \  
ln -s /root/.cargo/bin/rustdoc /usr/local/sbin/rustdoc && \  
ln -s /root/.cargo/bin/rustup /usr/local/sbin/rustup  
  
ENV TARGET=arm-unknown-linux-gnueabihf  
  
VOLUME /work  

