FROM mojodna/heroku-cedar:2.0.0  
  
ENV PATH $PATH:/.cabal/bin  
  
# libgmp hack  
RUN ln -s /usr/lib/libgmp.so.3 /usr/lib/libgmp.so  
# ghc  
RUN curl --silent
http://www.haskell.org/ghc/dist/7.6.3/ghc-7.6.3-x86_64-unknown-
linux.tar.bz2|tar xj \  
&& cd ghc-7.6.3/ && ./configure && make install && cd .. \  
&& rm -r ghc-7.6.3/ /usr/local/bin/haddock* /usr/local/lib/ghc-7.6.3/haddock
/usr/local/lib/ghc-7.6.3/html /usr/local/lib/ghc-7.6.3/latex
/usr/local/share/doc/ghc \  
&& echo "" > /usr/local/lib/ghc-7.6.3/ghc-usage.txt \  
&& echo "" > /usr/local/lib/ghc-7.6.3/ghci-usage.txt \  
&& find /usr/local/lib -name "*_p.a" -delete \  
&& find /usr/local/lib -name "*.p_hi" -delete \  
&& find /usr/local/lib -name "*.dyn_hi" -delete \  
&& find /usr/local/lib -name "*HS*.so" -delete \  
&& find /usr/local/lib -name "*HS*.o" -delete \  
&& find /usr/local/lib -name "*_debug.a" -delete \  
&& strip --strip-unneeded /usr/local/lib/ghc-7.6.3/runghc
/usr/local/lib/ghc-7.6.3/ghc  
# cabal-install & cabal update & happy  
RUN curl --silent http://hackage.haskell.org/package/cabal-
install-1.18.0.2/cabal-install-1.18.0.2.tar.gz|tar xz \  
&& cd cabal-install-1.18.0.2/ && sh bootstrap.sh && cd .. && rm -r cabal-
install-1.18.0.2/ \  
&& /.cabal/bin/cabal update && /.cabal/bin/cabal install happy  

