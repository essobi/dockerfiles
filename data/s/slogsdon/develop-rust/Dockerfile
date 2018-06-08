FROM slogsdon/develop-base  
  
ENV PATH $HOME/.cargo/bin:$PATH  
ENV RUST_SRC_PATH /usr/local/src/rust/src  
  
RUN \  
curl -sSf https://static.rust-lang.org/rustup.sh | sh &&\  
sudo mkdir -p $RUST_SRC_PATH &&\  
sudo git clone https://github.com/rust-lang/rust $RUST_SRC_PATH &&\  
cargo install racer  
  

