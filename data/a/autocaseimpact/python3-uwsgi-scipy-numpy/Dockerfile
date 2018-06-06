FROM paulflorea/python3-uwsgi:alpine  
  
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories;\  
echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories;\  
apk upgrade --update-cache --available  
  
# System dependencies  
RUN apk add ca-certificates gcc g++ curl openblas-dev  
  
# Create link to file for SciPy  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
  
RUN pip install numpy scipy

