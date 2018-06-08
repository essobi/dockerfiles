FROM pritunl/archlinux  
  
RUN pacman -S ca-certificates gcc musl upx rsync openssh --noconfirm  
  
RUN curl -sSf https://static.rust-lang.org/rustup.sh | \  
sh -s -- --channel=stable \  
\--with-target=x86_64-unknown-linux-musl \  
\--disable-sudo  
  
RUN mkdir /rust  
WORKDIR /rust  

