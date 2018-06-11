FROM debian:jessie  
  
ENV USER root  
ENV WORKDIR /rust/workspace  
  
USER $USER  
RUN apt-get update -y && apt-get upgrade -y  
  
# Dependecies for Rust  
RUN apt-get install curl file sudo gcc -y  
# Install Rust  
RUN curl -sf -L https://static.rust-lang.org/rustup.sh | sh  
  
RUN apt-get autoremove && apt-get autoclean && apt-get clean  
  
# Create and setup the workspace  
RUN mkdir -p $WORKDIR  
WORKDIR $WORKDIR

