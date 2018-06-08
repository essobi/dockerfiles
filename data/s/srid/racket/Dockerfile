FROM ubuntu  
  
ENV VERSION 6.1  
ADD http://mirror.racket-
lang.org/installers/${VERSION}/racket-${VERSION}-x86_64-linux-ubuntu-
precise.sh /racket.sh  
RUN bash /racket.sh  
  
ENV PATH /usr/racket/bin:$PATH  

