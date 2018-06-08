FROM node:6.3.0  
RUN npm install -g yo  
RUN adduser --disabled-password --gecos "" yo  
RUN git clone https://github.com/signed/generator-signed.git && cd generator-
signed && npm install -g && cd ..  
USER yo  
RUN yo --no-insight --help  
ENTRYPOINT ["yo"]  

