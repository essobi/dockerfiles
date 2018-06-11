FROM alpine:edge  
  
COPY install.sh /install.sh  
  
RUN apk --update add bash \  
&& /bin/bash /install.sh \  
&& rm /install.sh  
  
ENV HOME /root  
ENV PYENV_ROOT $HOME/.pyenv  
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH  

