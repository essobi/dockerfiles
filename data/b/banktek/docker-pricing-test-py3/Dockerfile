FROM frolvlad/alpine-python-machinelearning  
  
RUN apk add --no-cache \  
\--virtual=.build-dependencies \  
g++ gfortran file binutils \  
musl-dev python3-dev openblas-dev openldap-dev postgresql-dev && \  
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
find /usr/lib/python3.*/ -name 'tests' -exec rm -r '{}' \+ && \  
find /usr/lib/python3.*/site-packages/ -name '*.so' -print -exec sh -c 'file
"{}" | grep -q "not stripped" && strip -s "{}"' \; && \  
\  
rm /usr/include/xlocale.h && \  
\  
apk del .build-dependencies  
  
RUN apk add --no-cache git postgresql openldap  
RUN pip install -U tox pylint wheel make-deb boto3==1.3.0  
RUN adduser -D banktek;mkdir /apps;chown -R banktek /apps  
USER banktek  
WORKDIR /apps  
CMD echo "Welcome to pricing/docker-pricing-test-3 image..."  

