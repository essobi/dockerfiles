FROM hoverbear/archlinux  
MAINTAINER Andrew Hobden <andrew@hoverbear.org>  
  
# Install the Rust Repo  
RUN echo -e "[thestinger]\nSigLevel = Optional\nServer =
http://pkgbuild.com/~thestinger/repo/\$arch" >> /etc/pacman.conf  
RUN pacman -Sy rust-git git make --noconfirm  
RUN pacman -Scc  
RUN curl -O http://static.rust-lang.org/cargo-dist/cargo-nightly-linux.tar.gz  
RUN tar xf cargo-nightly-linux.tar.gz  
ENV PATH $PATH:/cargo-nightly/bin/  
  
# /source - Should mount the user code.  
# /build - Should be where the result goes.  
VOLUME [ "/source" ]  
  
# Change the Workdir to /source  
WORKDIR /source  

