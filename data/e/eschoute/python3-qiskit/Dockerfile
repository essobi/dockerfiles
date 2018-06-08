FROM eschoute/python3-matplotlib:0.0.2  
RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN apk --no-cache --update-cache add --virtual scipy-build \  
build-base freetype-dev lapack-dev pkgconfig gfortran libffi-dev openssl-dev
cmake  
RUN pip install --no-cache-dir 'scipy>=0.19,<1.1' # Separate install of scipy
for faster rebuilds.  
RUN pip install --no-cache-dir 'qiskit==0.4.9'  
RUN apk del scipy-build  
RUN apk add --no-cache --virtual scipy-runtime \  
freetype libgfortran libgcc libpng libstdc++ musl openblas tcl tk libffi
openssl lapack  

