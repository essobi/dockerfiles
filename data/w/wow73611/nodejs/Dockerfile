FROM wow73611/python  
MAINTAINER wow73611 <wow73611@gmail.com>  
  
RUN \  
wget http://nodejs.org/dist/node-latest.tar.gz && \  
tar xvzf node-latest.tar.gz && \  
cd node-v* && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd .. && \  
rm -f node-latest.tar.gz && \  
rm -rf node-v*  
  
RUN npm install -g npm  
ENV PATH node_modules/.bin:$PATH  
  
CMD ["node"]  

