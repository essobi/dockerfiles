FROM rust:1.23.0-jessie  
  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
RUN apt-get install -y nodejs  
  
RUN cargo install cargo-web  
RUN rustup target add wasm32-unknown-emscripten  
  
RUN mkdir /out /project  
  
# Ensure emscripten is downloaded and installed  
# Until something like `cargo web prepare-emscripten` exists  
COPY placeholder /tmp/placeholder  
RUN cd /tmp/placeholder && cargo web build --release --target-webasm-
emscripten  
RUN rm -r /tmp/placeholder  
  
ENV PROJECTDIR .  
  
COPY build-cargo-web.sh /bin/build-cargo-web.sh  
ENTRYPOINT [ "/bin/build-cargo-web.sh" ]  

