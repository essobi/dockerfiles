FROM clux/muslrust:nightly-2018-06-02  
  
RUN CARGO_BUILD_TARGET=x86_64-unknown-linux-gnu cargo install clippy \--force
\--vers 0.0.207 \--git https://github.com/rust-lang-nursery/rust-clippy.git
\--rev 1c6c79f92cad0c0e062ba1ef1d291f140e326cb3; \  
cargo \--version; \  
rustc \--version;  

