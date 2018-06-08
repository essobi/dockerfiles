FROM labios/base  
MAINTAINER Fabiano Menegidio <fabiano.menegidio@biology.bio.br>  
  
ENV PATH $HOME/.scienv/bin:$PATH  
  
RUN git clone https://github.com/LaBiOS/scienv.git $HOME/.scienv \  
&& echo 'export PATH="$HOME/.scienv/bin:$PATH"' >> ~/.bashrc \  
&& echo 'eval "$(scienv init -)"' >> ~/.bashrc \  
&& /bin/bash -c "exec $SHELL -l"  

