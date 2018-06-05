FROM meghait/puppet-ubuntu:latest  
  
MAINTAINER Michael Søby Andersen <michael@megha.it>  
  
# Install Haskell platform and Cabal.  
ADD puppet /tmp/puppet  
RUN cd /tmp/puppet; puppet apply -d manifests/default.pp
--modulepath=/tmp/puppet/modules  
  
USER cabal  
ENTRYPOINT ["/home/cabal/.cabal/bin/cabal"]  
WORKDIR /home/cabal/code  
CMD ["install", "-j", "--libdir=/home/cabal/lib", "--bindir=/home/cabal/bin"]  

