FROM crystallang/crystal:0.24.2  
# derived from ubuntu:xenial (16.04)  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
WORKDIR /workspace  
  
COPY rootfs/workspace/formatter.cr /workspace/formatter.cr  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

