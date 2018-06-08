FROM ubuntu:16.04  
  
MAINTAINER Jared Mackey <jared@mackey.tech>  
  
RUN apt-get update \  
&& apt-get install -y curl file build-essential  
  
RUN curl https://sh.rustup.rs -s > /home/install.sh && \  
chmod +x /home/install.sh && \  
sh /home/install.sh -y \--verbose \--default-toolchain nightly  
  
ENV PATH "/root/.cargo/bin:$PATH"  

