FROM httpd:2.4  
MAINTAINER "Kyle Bai <kyle.b@inwinstack.com>"  
# Install dependency packages  
RUN apt-get update && \  
apt-get install -y make g++ git curl  
  
# Install node.js  
RUN curl -sL https://deb.nodesource.com/setup_5.x | sh && \  
apt-get install -y nodejs  
  
# Install browser-solidity  
RUN git clone https://github.com/ethereum/browser-solidity.git && \  
cd browser-solidity && \  
npm install && npm run build && \  
mv ./* /usr/local/apache2/htdocs/ && \  
cd .. && rm -rf browser-solidity/  
  
# Show expose port  
EXPOSE 80/tcp  

