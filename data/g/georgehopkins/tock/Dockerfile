FROM debian:stretch  
  
RUN apt-get update -qq && \  
apt-get install -qqy build-essential cmake python ssh wget git unzip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN cd /opt && \  
wget -q "https://developer.arm.com/-/media/Files/downloads/gnu-
rm/6-2016q4/gcc-arm-none-
eabi-6_2-2016q4-20161216-linux.tar.bz2?product=GNU%20ARM%20Embedded%20Toolchain,64-bit,,Linux,6-2016-q4-major"
-O gcc.tar.bz2 && \  
tar -xjf gcc.tar.bz2  
ENV PATH "$PATH:/opt/gcc-arm-none-eabi-6_2-2016q4/bin"  
ENV RUSTUP_HOME=/usr/local/rustup \  
CARGO_HOME=/usr/local/cargo \  
PATH=/usr/local/cargo/bin:$PATH  
RUN wget -q "https://static.rust-lang.org/rustup/dist/x86_64-unknown-linux-
gnu/rustup-init" && \  
chmod +x rustup-init && \  
./rustup-init -y --no-modify-path --default-toolchain nightly-2018-04-19 && \  
rm rustup-init && \  
chmod -R a+w $RUSTUP_HOME $CARGO_HOME && \  
rustup --version && \  
cargo --version && \  
rustc --version  
  
RUN cd /opt && \  
wget -q
"https://github.com/uncrustify/uncrustify/archive/uncrustify-0.65.tar.gz" && \  
tar -xzf uncrustify-0.65.tar.gz && \  
cd uncrustify-uncrustify-0.65 && \  
mkdir build && \  
cd build && \  
cmake .. && \  
cmake --build .  
ENV PATH "$PATH:/opt/uncrustify-uncrustify-0.65/build"  
RUN cargo install --vers 0.6.0 --force rustfmt-nightly  
  
RUN cargo install xargo  

