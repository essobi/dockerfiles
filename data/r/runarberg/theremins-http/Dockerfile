FROM jimmycuadra/rust:1.5.0  
MAINTAINER Rúnar Berg "runarberg@zoho.com"  
EXPOSE 80  
ADD . /opt/source/  
RUN cd /opt/source && \  
cargo build --release && \  
ln -s /opt/source/target/release/theremins-http-server \  
/usr/local/bin/theremins-http-server  
  
CMD ["theremins-http-server", "--address", "0.0.0.0:80", "--ws-url",
"ws://ws.theremins.club"]  

