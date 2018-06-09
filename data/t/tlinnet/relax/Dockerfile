# docker build -t tlinnet/relax .  
FROM tlinnet/relax:10_relax  
  
# Update relax for python version 2.7. http://www.nmr-relax.com  
RUN cd $HOME && \  
cd $HOME/software/relax && \  
git pull && \  
/bin/bash -c "source activate python27; scons" && \  
/bin/bash -c "source activate python27; ./relax -i"

