FROM python:3-alpine  
MAINTAINER james.chevalier@commonmedia.com  
  
RUN apk add --update gcc libgfortran freetype-dev && \  
apk add --update --virtual=build_dependencies g++ gfortran make && \  
ln -s /usr/include/locale.h /usr/include/xlocale.h && \  
mkdir -p /tmp/build && \  
cd /tmp/build/ && \  
wget http://www.netlib.org/blas/blas-3.7.0.tgz && \  
wget http://www.netlib.org/lapack/lapack-3.7.0.tgz && \  
tar xzf blas-3.7.0.tgz && \  
tar xzf lapack-3.7.0.tgz && \  
cd /tmp/build/BLAS-3.7.0/ && \  
gfortran -O3 -std=legacy -m64 -fno-second-underscore -fPIC -c *.f && \  
ar r libfblas.a *.o && \  
ranlib libfblas.a && \  
mv libfblas.a /tmp/build/. && \  
cd /tmp/build/lapack-3.7.0/ && \  
sed -e "s/frecursive/fPIC/g" -e "s/ \\.\\.\// /g" -e
"s/^CBLASLIB/\\#CBLASLIB/g" make.inc.example > make.inc && \  
make lapacklib && \  
make clean && \  
mv liblapack.a /tmp/build/. && \  
cd / && \  
export BLAS=/tmp/build/libfblas.a && \  
export LAPACK=/tmp/build/liblapack.a && \  
pip install --no-cache-dir flask textblob scipy numpy scikit-learn pandas
matplotlib nltk && \  
python -m nltk.downloader punkt stopwords wordnet && \  
apk del \--purge -r build_dependencies && \  
rm -rf /tmp/build && \  
rm -rf /var/cache/apk/*  

