FROM fedora:latest  
MAINTAINER Ruben De Smet "me@rubdos.be"  
ARG VERSION_ARG  
  
# partof: #SPC-install-artifact  
RUN dnf groupinstall -y "C Development Tools and Libraries" && \  
dnf install -y curl file openssh-clients rsync pkgconf openssl openssl-devel
&& \  
curl https://sh.rustup.rs -sSf | \  
sh -s -- --default-toolchain stable -y && \  
$HOME/.cargo/bin/rustup run stable cargo install --root=/usr $VERSION_ARG
artifact-app && \  
$HOME/.cargo/bin/rustup self uninstall -y && \  
rm -rf ~./cargo ~/.rustup && \  
dnf group remove "C Development Tools and Libraries" -y && \  
dnf remove -y openssl-devel pkgconf && \  
dnf autoremove -y && \  
dnf clean all && rm -rf /var/cache/dnf  
# partof: #SPC-remove-cargo  
# partof: #SPC-implement-default-command  
CMD ["/root/.cargo/bin/art","ls"]  

