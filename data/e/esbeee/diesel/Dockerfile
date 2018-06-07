FROM scorpil/rust:1.15  
  
# Install dependencies.  
RUN apt-get update -qq && \  
apt-get install -y libpq-dev libsqlite3-dev libmysqlclient-dev  
  
# Install diesel_cli.  
RUN cargo install diesel_cli --vers 0.11.0  
ENV PATH /root/.cargo/bin:$PATH  

