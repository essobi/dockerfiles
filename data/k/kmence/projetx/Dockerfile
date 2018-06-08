FROM ubuntu  
MAINTAINER <herve leclerc> herve@jhhk.fr  
  
RUN mkdir /rust  
WORKDIR /rust  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt install -y \  
ca-certificates \  
curl \  
file \  
sudo \  
gcc \  
libc6-dev \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sf -L https://static.rust-lang.org/rustup.sh | sh  
  
  
#COPY hello.rs /rust/  
#RUN rustc hello.rs  
#CMD /rust/hello  

