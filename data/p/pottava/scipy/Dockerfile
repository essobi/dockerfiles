# SciPy v1.1 & NumPy v1.14.3  
#  
# docker run \--rm -it pottava/scipy:1.1  
# docker run \--rm pottava/scipy:1.1 -c 'import scipy;
print(scipy.__version__)'  
# docker run \--rm pottava/scipy:1.1 -c 'import scipy; scipy.show_config()'  
  
FROM alpine:3.7  
  
ENV SCIPY_VERSION=1.1.0 \  
BLAS=/usr/lib/libblas.so \  
LAPACK=/usr/lib/liblapack.so  
RUN apk --no-cache add openblas lapack libstdc++ python3 ca-certificates \  
&& apk --no-cache add --virtual build-deps lapack-dev python3-dev g++ gfortran
\  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& pip3 install "scipy == ${SCIPY_VERSION}" \  
&& find / -type d -name tests -depth -exec rm -rf {} \; \  
&& find / -type d -name test -depth -exec rm -rf {} \; \  
&& find / -type d -name \\__pycache__ -depth -exec rm -rf {} \; \  
&& find / -type d -name '*.egg-info' -depth -exec rm -rf {} \; \  
&& apk del --purge -r build-deps \  
&& rm -rf /root/.cache /usr/include/xlocale.h  
  
ENTRYPOINT ["python3"]  

