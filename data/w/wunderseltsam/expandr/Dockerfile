FROM darinmorrison/haskell  
  
RUN apt-get update && apt-get install zlib1g-dev  
  
RUN cabal update  
  
ADD . /usr/src/expandr  
  
RUN cd /usr/src/expandr && cabal install --bindir=/usr/bin  
  
EXPOSE 5000  
CMD ["expandr", "5000"]  

