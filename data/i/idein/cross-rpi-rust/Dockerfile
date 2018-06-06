  
FROM idein/cross-rpi:latest  
  
ARG RUST_CHANNEL=stable  
  
# rust toolchain  
ENV PATH $HOME/.cargo/bin:$PATH  
# cross compilation with rust  
ENV CC_arm_unknown_linux_gnueabihf armv6-rpi-linux-gnueabihf-gcc  
ENV PKG_CONFIG_ALLOW_CROSS=1  
USER root  
  
RUN apt-get -y update \  
&& apt-get -y --no-install-recommends install \  
git \  
ssh \  
libclang-3.9-dev \  
&& apt-get remove -y \  
&& rm -rf /var/lib/apt/lists \  
&& rm -rf /var/cache/apt/archives  
  
USER idein  
WORKDIR /home/idein  
  
RUN curl -sSfL https://sh.rustup.rs > rustup.sh \  
&& sh rustup.sh -y --default-toolchain ${RUST_CHANNEL}-x86_64-unknown-linux-
gnu \  
&& rustup toolchain install ${RUST_CHANNEL}-armv7-unknown-linux-gnueabihf \  
&& rustup target add arm-unknown-linux-gnueabihf  
  
CMD bash --login  
  

