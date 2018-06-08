FROM frolvlad/alpine-python2  
  
RUN apk add --no-cache \  
\--virtual=.build-dependencies \  
g++ gfortran file binutils \  
musl-dev python-dev openblas-dev && \  
apk add libstdc++ openblas && \  
\  
ln -s locale.h /usr/include/xlocale.h && \  
\  
pip install numpy && \  
pip install pandas && \  
pip install scipy && \  
pip install scikit-learn && \  
\  
rm -r /root/.cache && \  
find /usr/lib/python2.*/ -name 'tests' -exec rm -r '{}' \+ && \  
find /usr/lib/python2.*/site-packages/ -name '*.so' -print -exec sh -c 'file
"{}" | grep -q "not stripped" && strip -s "{}"' \; && \  
\  
rm /usr/include/xlocale.h && \  
\  
apk del .build-dependencies  
  
# Add pycddlib and cvxopt with GLPK  
RUN cd /tmp && \  
apk add --no-cache \  
\--virtual=.build-dependencies \  
gcc make file binutils \  
musl-dev python-dev gmp-dev suitesparse-dev openblas-dev && \  
apk add gmp suitesparse && \  
\  
pip install cython && \  
pip install pycddlib && \  
pip uninstall --yes cython && \  
\  
wget "ftp://ftp.gnu.org/gnu/glpk/glpk-4.65.tar.gz" && \  
tar xzf "glpk-4.65.tar.gz" && \  
cd "glpk-4.65" && \  
./configure --disable-static && \  
make -j4 && \  
make install-strip && \  
CVXOPT_BLAS_LIB=openblas CVXOPT_LAPACK_LIB=openblas CVXOPT_BUILD_GLPK=1 pip
install --global-option=build_ext --global-option="-I/usr/include/suitesparse"
cvxopt && \  
\  
rm -r /root/.cache && \  
find /usr/lib/python2.*/site-packages/ -name '*.so' -print -exec sh -c 'file
"{}" | grep -q "not stripped" && strip -s "{}"' \; && \  
\  
apk del .build-dependencies && \  
rm -rf /tmp/*  
  
RUN apk add --no-cache \  
\--virtual=.build-dependencies \  
g++ gfortran file binutils \  
musl-dev python-dev openblas-dev openldap-dev postgresql-dev && \  
apk add libstdc++ openblas && \  
\  
ln -s locale.h /usr/include/xlocale.h && \  
\  
pip install psycopg2-binary && \  
pip install python-ldap && \  
pip install bitarray && \  
pip install statsmodels && \  
\  
rm -r /root/.cache && \  
find /usr/lib/python2.*/ -name 'tests' -exec rm -r '{}' \+ && \  
find /usr/lib/python2.*/site-packages/ -name '*.so' -print -exec sh -c 'file
"{}" | grep -q "not stripped" && strip -s "{}"' \; && \  
\  
rm /usr/include/xlocale.h && \  
\  
apk del .build-dependencies  
  
RUN apk add --no-cache git postgresql openldap  
RUN pip install -U tox pylint wheel  
RUN adduser -D banktek;mkdir /apps;chown -R banktek /apps  
USER banktek  
WORKDIR /apps  
CMD echo "Welcome to pricing/docker-pricing-test-py2 image..."

