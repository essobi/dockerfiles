FROM dockcross/linux-x64  
MAINTAINER Erwin Gribnau "erwin@gribnau.org"  
  
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y  
RUN ln -s /root/.cargo/bin/cargo /usr/local/sbin/cargo && \  
ln -s /root/.cargo/bin/rustc /usr/local/sbin/rustc && \  
ln -s /root/.cargo/bin/rustdoc /usr/local/sbin/rustdoc && \  
ln -s /root/.cargo/bin/rustup /usr/local/sbin/rustup  
  
ENV TARGET=x86_64-unknown-linux-gnu  
  
VOLUME /work  

