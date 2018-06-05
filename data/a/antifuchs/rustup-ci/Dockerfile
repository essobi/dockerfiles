FROM liuchong/rustup:stable  
MAINTAINER Andreas Fuchs <asf@boinkor.net>  
  
RUN cargo install cargo-kcov --force  
RUN apt-get update  
RUN apt-get install -y wget cmake libcurl4-openssl-dev libelf-dev libdw-dev
build-essential pkg-config libbfd-dev libiberty-dev  
RUN apt-get install -y zlib1g-dev python  
RUN eval "$(cargo kcov --print-install-kcov-sh)"  

