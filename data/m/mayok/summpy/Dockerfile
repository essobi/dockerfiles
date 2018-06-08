FROM alpine:edge  
  
RUN apk update \  
&& apk add python2 \  
py2-pip \  
python-dev \  
ca-certificates \  
&& apk add --virtual=build-deps \  
gfortran \  
g++ \  
make \  
gcc \  
&& rm -rf /var/cache/apk/*  
  
# For scipy compilation, blas and lapack is necessary  
RUN mkdir ~/src/  
WORKDIR src  
  
RUN wget http://www.netlib.org/blas/blas-3.7.0.tgz  
RUN wget http://www.netlib.org/lapack/lapack-3.7.0.tgz  
RUN tar xfz blas-3.7.0.tgz  
RUN tar xfz lapack-3.7.0.tgz  
  
# BLAS  
RUN cd BLAS-3.7.0 \  
&& gfortran -O3 -std=legacy -m64 -fno-second-underscore -fPIC -c *.f \  
&& ar r libfblas.a *.o \  
&& ranlib libfblas.a \  
&& rm -rf *.o  
ENV BLAS=/src/BLAS-3.7.0/libfblas.a  
  
# LAPACK  
RUN cd lapack-3.7.0 \  
&& sed -e "s/frecursive/fPIC/g" -e "s/ \\.\\.\// /g" -e
"s/^CBLASLIB/\\#CBLASLIB/g" make.inc.example > make.inc \  
&& make lapacklib \  
&& make clean  
ENV LAPACK=/src/lapack-3.7.0/liblapack.a  
  
WORKDIR /root  
  
# Fix numpy compilation  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
  
RUN pip install summpy janome  
  
# Cleanup  
RUN apk del build-deps && rm -r /root/.cache /src  
  
EXPOSE 8080  
ENTRYPOINT ["python2", "-m summpy.server"]  
CMD ["-h", "127.0.0.1", "-p", "8080"]  

