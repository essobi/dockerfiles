FROM alpine:3.4  
MAINTAINER Gabriel Almeida<gabriel_almeida@me.com>  
  
# Install build-deps and deps. Using emacs from testing@edge repo as its  
# unavailable elsewhere  
RUN apk add --update -t build-deps tar curl \  
&& apk add -t deps --update-cache --allow-untrusted \  
\--repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \  
make emacs  
  
# Download & install orgmk  
RUN mkdir orgmk \  
&& curl -sL
https://github.com/fniessen/orgmk/tarball/41689e1feda70b5ff5bb41e1cd3f5d916a1c776a
\  
| tar xzC orgmk --strip-components=1 \  
&& ( \  
cd orgmk \  
&& make \  
&& make install \  
) \  
&& touch download-emacs-deps.org \  
&& org2html download-emacs-deps.org \  
&& rm -f download-emacs-deps.org download-emacs-deps.html \  
&& apk del build-deps  
  
WORKDIR "${PWD}/orgmk/bin"  
CMD "./org2html"  

