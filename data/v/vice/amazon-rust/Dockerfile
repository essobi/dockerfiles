FROM amazonlinux  
  
ARG DEFAULT_TOOLCHAIN=stable  
ARG NIGHTLY_TOOLCHAIN=nightly  
  
ENV PATH=/usr/local/cargo/bin:$PATH \  
CARGO_HOME=/usr/local/cargo \  
RUSTUP_HOME=/usr/local/rustup  
  
RUN yum update -y \  
&& yum install -y gcc g++ git make openssl-devel \  
&& curl https://sh.rustup.rs -sSf | sh -s -- \  
\--default-toolchain $DEFAULT_TOOLCHAIN \  
\--no-modify-path \  
-y \  
&& chmod -R a+w $RUSTUP_HOME $CARGO_HOME \  
&& rustup install $NIGHTLY_TOOLCHAIN \  
&& cargo install cargo-make \  
&& cargo install cargo-watch \  
&& cargo +$NIGHTLY_TOOLCHAIN install clippy \  
&& cargo +$NIGHTLY_TOOLCHAIN install rustfmt-nightly \  
&& yum clean all  
  
# Install python and awscli  
RUN yum install -y python \  
&& curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py \  
&& pip install -q awscli \--upgrade \  
&& aws \--version  

