FROM dmoj/judge-base-medium:latest  
  
RUN apt-get install -y --no-install-recommends \  
bzip2 && \  
apt-get clean  
  
RUN wget -q -O- --no-check-certificate
https://bitbucket.org/pypy/pypy/downloads/pypy-4.0.1-linux64.tar.bz2 | \  
tar -xjC /opt && \  
rm -rf /opt/pypy-4.0.1-linux64/lib-python/test  
  
RUN wget -q -O- --no-check-certificate
https://bitbucket.org/pypy/pypy/downloads/pypy3-2.4.0-linux64.tar.bz2 | \  
tar -xjC /opt && \  
rm -rf /opt/pypy3-2.4.0-linux64/lib-python/3/test  

