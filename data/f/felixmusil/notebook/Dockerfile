FROM felixmusil/notebook:custom  
  
USER $NB_USER  
  
RUN cd $HOME/git/ \  
&& git clone https://github.com/cosmo-epfl/sketchmap.git \  
&& cd $HOME/git/sketchmap \  
&& git checkout 7e059bd5524bba678f3cd9f7c359942a9dce7823 \  
&& make \  
&& mkdir $HOME/bin \  
&& cp $HOME/git/sketchmap/bin/* $HOME/bin/  
  
USER root  
  
RUN echo 'export PATH=$PATH:$HOME/bin' >> /etc/bash.bashrc  
  
Run echo 'alias sketchmap="$HOME/git/sketchmap/utils/sketch-map.sh"' >>
/etc/bash.bashrc  
  
USER $NB_USER

