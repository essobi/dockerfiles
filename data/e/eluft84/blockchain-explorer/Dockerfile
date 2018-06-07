FROM node:6  
MAINTAINER Eugen Luft <eugeluft@de.ibm.com>  
  
EXPOSE 8080  
WORKDIR blockchain-explorer  
  
# Download latest master of Hyperledger Version  
RUN wget https://github.com/hyperledger/blockchain-
explorer/archive/master.tar.gz \  
&& tar -xvzf master.tar.gz --strip 1 \  
&& rm -Rf master.tar.gz  
  
# Install npm dependencies  
RUN npm install  
  
COPY wait-for-it.sh wait-for-it.sh  
RUN chmod 775 wait-for-it.sh  
  

