# Copyright 2017 Aldrin J D'Souza.  
# Licensed under the MIT License <https://opensource.org/licenses/MIT>  
# Rust CI Image  
FROM rust  
  
# Install kcov  
RUN apt-get -y update && apt-get -q -y upgrade  
RUN apt-get install -y --fix-missing pkg-config  
RUN apt-get install -y zlib1g wget libcurl4-openssl-dev libelf-dev libdw-dev
cmake cmake-data g++ binutils-dev libiberty-dev zlib1g-dev python-minimal git  
  
# Externalize kcov location  
ARG KCOV=34  
ADD https://github.com/SimonKagstrom/kcov/archive/v$KCOV.tar.gz
/kcov/src.tar.gz  
RUN cd /kcov && tar xf src.tar.gz && mkdir build && cd build && cmake ../kcov*
&& make && make install  
  
# Install jq (required for extracting test file names)  
RUN apt-get -y install jq  
  
# Update the rust toolkit  
RUN rustup update stable  
RUN rustup update nightly  
  
# Install required Rust tools  
RUN cargo install cargo-audit  
RUN cargo install cargo-tree  
RUN cargo install just  
RUN rustup run nightly cargo install clippy  
  
# Add the Justfile  
ADD Justfile /  
  
# Volume  
VOLUME /src  
  
# Entrypoint  
ENTRYPOINT ["just", "-d", "/src", "--justfile", "/Justfile"]  
CMD ["check"]  

