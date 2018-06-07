FROM liuchong/rustup:nightly  
MAINTAINER Philip Jackson <p-jackson@live.com>  
  
RUN apt-get update -qq && \  
apt-get install -y libpq-dev libsqlite3-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN cargo install diesel_cli  
  
RUN rustc --version  
RUN cargo --version  
RUN diesel --version  

