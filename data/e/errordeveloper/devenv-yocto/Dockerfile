FROM errordeveloper/devenv-yocto:base  
  
ENV CHACHE_REPOS git://git.yoctoproject.org/poky  
RUN mkdir -p repos  
RUN bash -c 'cd repos/; for repo in ${CHACHE_REPOS}; do (git clone --quiet
--bare --mirror $repo || echo "Failed to clone $repo"); done'  

