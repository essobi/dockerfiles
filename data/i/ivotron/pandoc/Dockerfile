FROM ivotron/texlive:20160320-1  
MAINTAINER Ivo Jimenez <ivo.jimenez@gmail.com>  
  
RUN apt-get -yq update && apt-get install -y haskell-platform && \  
cabal update && \  
mkdir pandoc-crossref && \  
cd pandoc-crossref && \  
cabal sandbox init && \  
cabal install pandoc-crossref-0.2.1.3 && \  
cabal install pandoc-citeproc && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV PATH=/pandoc-crossref/.cabal-sandbox/bin:$PATH  
ENTRYPOINT ["pandoc"]  
CMD ["--help"]  

