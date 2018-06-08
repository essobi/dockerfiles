FROM rust:1.25.0-stretch  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
COPY rootfs/workspace/rust /workspace/rust  
RUN chown -R codewarrior:codewarrior /workspace/rust  
  
WORKDIR /workspace  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior \  
# Allow dead_code to avoid tests from printing warnings about private
identifiers  
RUSTFLAGS='-Adead_code'  
# download and compile crates  
RUN set -ex; \  
cd /workspace/rust; \  
cargo build; \  
rm src/lib.rs;  

