#####################################################  
# Build an image for compiling safe_vault for AMD64 #  
# using the musl STD library #  
#####################################################  
  
  
# Set the base image to Debian  
FROM debian:jessie  
  
  
# Set this to avoid warning messages.  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Create a working folder.  
  
RUN mkdir /projects  
  
  
# Install the GCC toolchain and various other tools:  
  
RUN apt-get update && apt-get -y upgrade && apt-get -y install \  
autoconf \  
build-essential \  
curl \  
git \  
libtool \  
pkg-config \  
tar \  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
# Install the musl standard libraries and the musl-gcc wrapper:  
  
RUN cd /projects \  
&& git clone git://git.musl-libc.org/musl \  
&& cd musl \  
&& ./configure --disable-shared \  
&& make && make install \  
&& cd /projects \  
&& rm -rf musl  
  
  
# Make sure that musl-gcc is on your PATH by putting a symbolic link  
# in a folder that is on the PATH:  
  
RUN ln -s /usr/local/musl/bin/musl-gcc /usr/local/bin/musl-gcc  
  
  
# Install the Sodium system library (libsodium):  
  
ENV PKG_CONFIG_ALLOW_CROSS 1  
  
RUN cd /projects \  
&& git clone https://github.com/jedisct1/libsodium.git \  
&& cd libsodium \  
&& ./autogen.sh \  
&& CC=musl-gcc ./configure --enable-shared=no \  
&& make && make install \  
&& cd /projects \  
&& rm -rf libsodium  
  
  
# Set up the Rust compile environment:  
  
ENV PATH /root/.cargo/bin:$PATH  
  
RUN cd /projects \  
&& curl https://sh.rustup.rs -o rustup.sh \  
&& chmod +x /projects/rustup.sh \  
&& /projects/rustup.sh -y \  
&& rustup target add x86_64-unknown-linux-musl  
  
  
# Create the compile script:  
  
RUN printf '#! /bin/sh\n\nexport PKG_CONFIG_ALLOW_CROSS=1\nrm -f /done123\ncd
/projects\nrm -rf safe_vault\ngit clone
http://github.com/maidsafe/safe_vault\ncd safe_vault\ncargo build --release
--target=x86_64-unknown-linux-musl\ntouch /done123\n' > /compile  
  
RUN chmod +x /compile  
  
  
# Testing only: Build safe_vault and copy the safe_vault binary to root dir.  
  
#RUN /compile \  
# && cp /projects/safe_vault/target/x86_64-unknown-linux-
musl/release/safe_vault / \  
# && rm -rf /projects/safe_vault \  
# && rm -rf /root/.cargo/registry/*  
  
  
# Remove compile-finished-flag file:  
  
RUN rm -f /done123  
  

