FROM amazonlinux:latest  
  
ARG TOOLCHAIN=stable  
ARG LIBSODIUM=1.0.16  
RUN yum -y update && \  
yum -y groupinstall "Development Tools" && \  
yum -y install sudo && \  
useradd rust -u 1000 --user-group --create-home --shell /bin/bash --groups
wheel  
  
RUN curl
https://nodejs.org/download/release/v6.11.3/node-v6.11.3-linux-x64.tar.xz |
tar --strip-components 1 -Jx -C /usr/  
  
# Allow sudo without a password.  
ADD sudoers /etc/sudoers.d/nopasswd  
  
# Run all further code as user `rust`, and create our working directories  
# as the appropriate user.  
USER rust  
RUN mkdir -p /home/rust/libs /home/rust/src  
  
ENV
PATH=/home/rust/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
ENV PKG_CONFIG_PATH=/usr/local/lib/pkgconfig  
ENV LD_LIBRARY_PATH=/usr/local/lib  
  
RUN curl https://sh.rustup.rs -sSf | \  
sh -s -- -y --default-toolchain $TOOLCHAIN && \  
rustup toolchain install $TOOLCHAIN && \  
rustup component add rustfmt-preview  
  
# Download & extract & make libsodium  
# Move libsodium build  
RUN \  
cd ~ && \  
curl
https://download.libsodium.org/libsodium/releases/libsodium-$LIBSODIUM.tar.gz
| tar -xz && \  
cd libsodium-$LIBSODIUM/ && \  
./configure && make && sudo make install && \  
sudo mv src/libsodium /usr/local/ && \  
rm -Rf ~/libsodium-$LIBSODIUM  
  
# Expect our source code to live in /home/rust/src. We'll run the build as  
# user `rust`, which will be uid 1000, gid 1000 outside the container.  
WORKDIR /home/rust/src  
  

