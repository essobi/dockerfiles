FROM node:9.10.1  
ARG builddir=/root/build  
WORKDIR ${builddir}  
ENV PATH="/root/.cargo/bin:${PATH}"  
RUN apt-get update -q && apt-get install -y jq musl  
  
# Install Rust  
COPY rust-toolchain ${builddir}/rust-toolchain  
RUN curl https://sh.rustup.rs -sSf | bash -s -- --default-toolchain=$(cat
rust-toolchain) -y  
RUN rustup target add wasm32-unknown-unknown --toolchain $(cat rust-toolchain)  
RUN rustup target add x86_64-unknown-linux-musl --toolchain $(cat rust-
toolchain)  
  
# Install wasm-gc  
RUN cargo install wasm-gc -f  
  
# Copy Rust package configuration  
COPY Cargo.toml Cargo.lock build.rs ${builddir}/  
COPY src/lib.rs ${builddir}/src/lib.rs  
COPY semantic/Cargo.toml ${builddir}/semantic/Cargo.toml  
COPY semantic/src/lib.rs ${builddir}/semantic/src/lib.rs  
COPY semantic-derive/Cargo.toml ${builddir}/semantic-derive/Cargo.toml  
COPY semantic-derive/src/lib.rs ${builddir}/semantic-derive/src/lib.rs  
  
# Install wasm-bindgen  
RUN cargo install --git https://github.com/alexcrichton/wasm-bindgen.git --rev
$(cargo read-manifest --locked | jq '.dependencies[]|select(.name == "wasm-
bindgen")|.source' -r | cut -d= -f2) -f  
  
# Copy everything  
COPY . ${builddir}/  
  
# Full build  
RUN yarn  
RUN yarn build  
  
FROM debian:stretch-slim  
ENTRYPOINT ["/usr/bin/se"]  
COPY \--from=0 /root/build/target/release/se /usr/bin/se  

