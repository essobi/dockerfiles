## Dockerfile for optimized elm version 0.16  
FROM haskell:7.10.2 as builder  
MAINTAINER Kuba Łopuszański <qbolec@gmail.com>  
  
ENV PATH $PATH:/elm/Elm-Platform/optimized/.cabal-sandbox/bin  
WORKDIR elm  
RUN apt-get update  
RUN apt-get -y install curl  
RUN apt-get -y install git-core  
RUN curl https://raw.githubusercontent.com/qbolec/elm-
platform/optimized/installers/BuildNoProfiling.hs > BuildNoProfiling.hs  
RUN runhaskell BuildNoProfiling.hs optimized  
  
FROM debian:jessie  
WORKDIR elm  
COPY \--from=builder /elm/Elm-Platform/optimized/.cabal-sandbox/bin .  
ENV PATH $PATH:/elm  
RUN apt-get update  
# Without the next line running elm-make failed with:  
# elm-make: error while loading shared libraries: libgmp.so.10: cannot open
shared object file: No such file or directory  
RUN apt-get -y install libgmp3-dev  
# Without the next line building Haukka from scratch (without elm-staff
directory) failed with:  
# Downloading NoRedInk/elm-decode-pipeline  
# failed with 'TlsExceptionHostPort (HandshakeFailed (Error_Protocol
("certificate has unknown CA",True,UnknownCa))) "github.com" 80' when sending
request to  
# <http://github.com/NoRedInk/elm-decode-pipeline/zipball/1.1.1/>  
RUN apt-get -y install ca-certificates  
# See: https://github.com/elm-lang/elm-make/issues/33#issuecomment-134214893  
# the problem was that without the following line compilation of Haukka failed
with  
# elm-make: elm-stuff/packages/elm-lang/core/3.0.0/src/Graphics/Element.elm:
hGetContents: invalid argument (invalid byte sequence)  
ENV LC_ALL C.UTF-8  
ENTRYPOINT ["elm-make"]  
  

