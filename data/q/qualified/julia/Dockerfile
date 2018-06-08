FROM julia:0.6.0  
# derived from debian:jessie  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
WORKDIR /workspace  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  
  
COPY rootfs/usr /usr  

