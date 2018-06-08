FROM ruby:2.4.2-slim-stretch  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
# bash/dash is installed already  
# csh/tcsh for backward compatibility  
# csh 20110502-2.2+b1  
csh \  
# tcsh 6.20.00-7  
# (csh + programmable command-line completion/editing, etc)  
tcsh \  
# extra utilities  
bc \  
mlocate \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
RUN gem install \  
rspec:3.6.0 \  
faker:1.8.4  
  
COPY rootfs/runner /runner  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  
WORKDIR /workspace  

