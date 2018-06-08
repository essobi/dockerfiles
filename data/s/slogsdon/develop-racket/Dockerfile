FROM slogsdon/develop-base  
  
ENV RACKET_VERSION 6.5  
RUN \  
curl -O https://mirror.racket-
lang.org/installers/$RACKET_VERSION/racket-$RACKET_VERSION-x86_64-linux.sh &&\  
sudo sh racket-$RACKET_VERSION-x86_64-linux.sh \  
\--unix-style \  
\--dest /usr/local \  
&&\  
rm racket-$RACKET_VERSION-x86_64-linux.sh  

