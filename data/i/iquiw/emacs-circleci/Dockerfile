FROM debian:stretch  
  
ENV DEBIAN_FRONTEND=noninteractive  
ENV EMACS_PACKAGE=emacs24-nox  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends ca-certificates curl git python ssh
"$EMACS_PACKAGE" && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -fsSL https://raw.github.com/cask/cask/master/go | python  
  
ENV PATH=/root/.cask/bin:$PATH  

