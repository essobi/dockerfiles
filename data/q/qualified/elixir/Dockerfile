FROM elixir:1.6.4-alpine  
  
RUN set -ex; \  
adduser -D codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
WORKDIR /workspace  
  
COPY rootfs/workspace /workspace  
RUN chown -R codewarrior:codewarrior /workspace  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

