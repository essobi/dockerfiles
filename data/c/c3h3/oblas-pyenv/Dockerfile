  
FROM c3h3/openblas:u1404  
  
ENV HOME /root  
ENV PYENVPATH $HOME/.pyenv  
ENV PATH $PYENVPATH/shims:$PYENVPATH/bin:$PATH  
  
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-
installer/master/bin/pyenv-installer | bash  
  
RUN echo 'eval "$(pyenv init -)"' > /root/.bashrc  
  

