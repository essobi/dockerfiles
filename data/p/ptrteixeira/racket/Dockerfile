FROM buildpack-deps:jessie-curl  
  
ENV RACKET_SHA1 d79e18dd039ed8a37f724e06655316413ef4261b  
  
RUN wget -qO /tmp/racket.sh https://mirror.racket-
lang.org/installers/6.12/racket-6.12-x86_64-linux.sh && \  
/bin/sh /tmp/racket.sh >> /dev/null && \  
rm /tmp/racket.sh  
  
ENV PATH /usr/racket/bin:$PATH  
ENTRYPOINT ["racket"]  
CMD ["--version"]  

