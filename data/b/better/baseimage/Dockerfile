FROM better/baseimage:alpine-3.7  
LABEL variant="analytics"  
  
RUN apk add --no-cache libffi-dev \  
postgresql \  
postgresql-client \  
postgresql-dev \  
postgresql-libs \  
postgresql-contrib  
  
# Matplotlib dependencies from
https://gist.github.com/orenitamar/f29fb15db3b0d13178c1c4dd611adce2  
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN apk --no-cache --update-cache add gfortran build-base wget freetype-dev
libpng-dev openblas-dev  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
  
RUN pip3 install matplotlib==2.0.2 \  
pandas==0.22.0 \  
psycopg2==2.7.2 \  
scipy==1.0.1 \  
seaborn==0.8 \  
https://github.com/better/alpine-
tensorflow/releases/download/alpine3.7-tensorflow1.7.0/tensorflow-1.7.0-cp36-cp36m-linux_x86_64.whl
\  
&& pip3 install scikit-learn==0.19.1 # Something with scikit-learn requires it
to be installed *after* scipy.  
  
# Make sure all the libraries are installed properly  
RUN python3 -c 'import matplotlib, pandas, psycopg2, seaborn, sklearn,
tensorflow'  

