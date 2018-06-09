FROM ubuntu:16.04  
EXPOSE 8000  
RUN apt-get update && \  
apt-get install -y curl \  
build-essential \  
git \  
curl \  
cmake \  
libsqlite3-dev  
  
ENV PATH $PATH:/root/.cargo/bin  
  
RUN curl https://sh.rustup.rs -sSf |curl https://sh.rustup.rs -sSf | sh -s --
--default-toolchain nightly -y && \  
rustup install nightly && \  
rustup default nightly  
  
WORKDIR /usr/src/stationapi  
COPY . .  
RUN cargo install  
  
CMD ["stationapi"]

