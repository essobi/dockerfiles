FROM wunderseltsam/constraint-solvers AS build-z3  
  
FROM alpine:3.6 AS build-lh  
# INSTALL BASIC DEV TOOLS, GHC, GMP & ZLIB  
RUN apk --update add alpine-sdk git ca-certificates ghc gmp-dev zlib-dev  
  
# GRAB A RECENT BINARY OF STACK  
RUN curl -sSL https://get.haskellstack.org/ | sh  
  
# COMPILE  
# COPY liquidhaskell /tmp/liquidhaskell  
WORKDIR /tmp/  
RUN git clone \--recursive -b master https://github.com/ucsd-
progsys/liquidhaskell.git  
WORKDIR liquidhaskell  
RUN stack --local-bin-path /sbin install --system-ghc  
  
# cabal  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories  
RUN apk --update add cabal  
RUN cabal update  
RUN cabal install vector --global  
  
# COMPRESS WITH UPX  
RUN apk add upx=3.94-r0  
RUN upx --best --ultra-brute /sbin/fixpoint  
RUN upx --best --ultra-brute /sbin/liquid  
RUN upx --best --ultra-brute /sbin/target  
  
FROM alpine:3.6  
RUN apk --update --no-cache add gcc gmp-dev zlib-dev libffi-dev  
COPY \--from=build-lh /usr/lib/ghc-8.0.2/ /usr/lib/ghc-8.0.2/  
COPY \--from=build-lh /usr/local/lib/x86_64-linux-ghc-8.0.2/
/usr/local/lib/x86_64-linux-ghc-8.0.2/  
COPY \--from=build-lh /sbin/liquid /sbin/liquid  
COPY \--from=build-lh /sbin/fixpoint /sbin/fixpoint  
COPY \--from=build-lh /sbin/target /sbin/target  
COPY \--from=build-lh /tmp/liquidhaskell/.stack-
work/install/x86_64-linux/lts-8.9/8.0.2/share/x86_64-linux-
ghc-8.0.2/liquidhaskell-0.8.0.5/ /tmp/liquidhaskell/.stack-
work/install/x86_64-linux/lts-8.9/8.0.2/share/x86_64-linux-
ghc-8.0.2/liquidhaskell-0.8.0.5/  
COPY \--from=build-z3 /usr/local/bin/z3 /sbin/z3

