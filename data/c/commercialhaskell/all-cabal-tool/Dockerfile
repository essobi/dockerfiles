FROM fpco/stack-run:lts-7  
  
COPY run.sh /usr/local/bin/run.sh  
  
RUN curl https://s3.amazonaws.com/stackage-travis/all-cabal-tool/all-cabal-
tool.bz2 | bunzip2 > /usr/local/bin/all-cabal-tool && \  
chmod +x \  
/usr/local/bin/run.sh \  
/usr/local/bin/all-cabal-tool  

