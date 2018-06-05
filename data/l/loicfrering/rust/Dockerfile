FROM debian:jessie  
MAINTAINER Loïc Frering <loic.frering@gmail.com>  
  
# Install common packages  
RUN apt-get update && apt-get install -y \  
gcc \  
curl \  
file \  
locales \  
libssl-dev  
  
# Install Rust  
RUN curl -sSf https://static.rust-lang.org/rustup.sh | sh -s -- --disable-sudo
--yes  
  
# Set the locale  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
# Working directory  
WORKDIR /work  
  
# Default command  
CMD ["bash"]  

