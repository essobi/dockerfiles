FROM ubuntu  
MAINTAINER Kevin Traver "kevintraver@gmail.com"  
RUN apt-get update && \  
apt-get install \  
ca-certificates \  
curl \  
git \  
gcc \  
libc6-dev \  
-qqy \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV RUST_ARCHIVE=rust-nightly-x86_64-unknown-linux-gnu.tar.gz  
ENV RUST_DOWNLOAD_URL=https://static.rust-lang.org/dist/$RUST_ARCHIVE  
  
RUN mkdir -p /rust  
WORKDIR /rust  
  
RUN git clone https://github.com/kevintraver/fuzzy_clock_rust.git  
  
RUN curl -fsOSL $RUST_DOWNLOAD_URL \  
&& curl -s $RUST_DOWNLOAD_URL.sha256 | sha256sum -c - \  
&& tar -C /rust -xzf $RUST_ARCHIVE \--strip-components=1 \  
&& rm $RUST_ARCHIVE \  
&& ./install.sh  
  
ADD Cargo.toml Cargo.toml  
ADD src src  
ADD Rocket.toml Rocket.toml  
  
EXPOSE 8080  
ENV ROCKET_ENV=production  
  
RUN cargo build --release  
  
ENTRYPOINT ["./target/release/fuzzy_clock_rust", "--server"]  

