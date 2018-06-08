FROM buildpack-deps:jessie  
  
RUN apt-get update && apt-get install libudev-dev -y \  
&& curl -sSf https://static.rust-lang.org/rustup.sh | sh -s -- --disable-sudo
\  
&& cargo install --git https://github.com/paritytech/parity.git parity --tag
v1.7.0 \  
&& strip /root/.cargo/bin/parity \  
&& cp -v /root/.cargo/bin/parity /usr/local/bin/ \  
&& /usr/local/lib/rustlib/uninstall.sh \  
&& rm -rf /root/.cargo/ \  
&& rm -rf /var/lib/apt/lists/*  

