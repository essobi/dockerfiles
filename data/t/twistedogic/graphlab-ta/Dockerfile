FROM twistedogic/graphlab  
MAINTAINER Jordan Li  
RUN wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz &&
\  
tar -xvzf ta-lib-0.4.0-src.tar.gz && \  
cd ta-lib/ && \  
./configure --prefix=/usr && \  
make && \  
make install  
# Python wrapper  
RUN git clone https://github.com/mrjbq7/ta-lib.git && cd ta-lib && python
setup.py install  

