ARG PATH_DLSHOGI=/opt/local/python-dlshogi  
  
FROM chainer/chainer:v3.3.0-python3  
RUN pip3 install python-shogi  
  
ARG PATH_DLSHOGI  
ADD cpu-only.tar.gz $PATH_DLSHOGI  
RUN pip3 install -e $PATH_DLSHOGI

