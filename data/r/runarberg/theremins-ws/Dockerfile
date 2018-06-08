FROM jimmycuadra/rust:1.5.0  
MAINTAINER Rúnar Berg "runarberg@zoho.com"  
EXPOSE 80  
ADD . /opt/source/  
RUN cd /opt/source && \  
cargo build --release && \  
ln -s /opt/source/target/release/theremins-ws-server \  
/usr/local/bin/theremins-ws-server  
  
CMD ["theremins-ws-server", "--address", "0.0.0.0:80"]  

