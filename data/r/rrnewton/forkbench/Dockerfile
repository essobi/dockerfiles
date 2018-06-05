FROM parfunc/compile-o-rama:0.2.4  
# Go ahead and prefetch/build dependencies BEFORE adding the bulk of  
# the files to the container:  
# ------------------------------------------------------------------  
ADD stack.yaml /forkbench/  
ADD Makefile /forkbench/  
WORKDIR /forkbench/  
RUN stack --system-ghc setup  
# RUN mkdir /forkbench/cloud-haskell /forkbench/io-threads /forkbench/ghc-
sparks /forkbench/monad-par  
ADD cloud-haskell/forkbench-cloud-haskell.cabal /forkbench/cloud-haskell/  
ADD io-threads/forkbench-io-threads.cabal /forkbench/io-threads/  
ADD ghc-sparks/forkbench-ghc-sparks.cabal /forkbench/ghc-sparks/  
ADD monad-par/forkbench-monad-par.cabal /forkbench/monad-par/  
RUN stack --system-ghc build --only-dependencies  
# ------------------------------------------------------------------  
# # See clean_checkout in the Makefile for how to make sure this isn't too
much data:  
ADD . /forkbench  
  
RUN make build  
  
RUN apt-get update && apt-get -y install tree jq gnuplot  
# RUN make build-cilk  
# # RUN make build-rust  
# # RUN make build-hpx  

