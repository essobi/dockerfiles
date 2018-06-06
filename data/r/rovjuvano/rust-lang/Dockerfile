FROM rovjuvano/rust-lang-base:1  
  
RUN : \  
&& curl -o dist.tar.gz -L https://static.rust-
lang.org/dist/rust-1.5.0-x86_64-unknown-linux-gnu.tar.gz \  
&& tar xzf dist.tar.gz \  
&& sh rust-*/install.sh --components=rustc,cargo \  
&& rm -rf dist rust-* \  
&& :  

