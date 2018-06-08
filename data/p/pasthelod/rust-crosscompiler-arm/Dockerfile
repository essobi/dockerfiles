FROM debian:testing  
  
COPY ./setup.sh /tmp/container-setup.sh  
  
RUN bash -x /tmp/container-setup.sh  
  
VOLUME ["/root/.cargo/git", "/root/.cargo/registry"]  
  
VOLUME ["/source"]  
WORKDIR /source  
  
CMD ["supercargo", "-v"]  
  

