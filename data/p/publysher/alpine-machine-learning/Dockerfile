FROM python:3.6-alpine3.7  
  
RUN apk --no-cache add lapack && apk --no-cache add \--virtual builddeps g++
gfortran musl-dev lapack-dev && pip install numpy && pip install scipy && pip
install scikit-learn==0.19.1 pandas==0.22.0 && apk del builddeps && rm -rf
/root/.cache  

