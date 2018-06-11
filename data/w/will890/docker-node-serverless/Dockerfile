FROM amazonlinux:latest  
  
  
RUN yum install -y git  
RUN yum install -y gcc-c++ make  
RUN yum install -y openssl-devel  
RUN git clone https://github.com/nodejs/node.git  
RUN cd ./node/ && ls -l && git checkout v6.10.2 && git checkout v6.10.2 &&
./configure && make && make install  
  
RUN npm -v  
RUN yum install -y wget  
RUN wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz  
RUN tar -xvf ./wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
RUN cd /wkhtmltox/bin && cp wkhtmltopdf /usr/bin/wkhtmltopdf  
RUN rm -r ./wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
  
ENV PATH="/usr/bin/wkhtmltopdf:${PATH}"  
RUN echo "$PATH"  
  
RUN npm install -g node-wkhtmltopdf  
RUN npm install -g serverless@1.16.1  
RUN serverless -v  
  
ENV LDFLAGS=-Wl,-rpath=/var/task/  
RUN yum install cairo cairo-devel libjpeg8-devel libjpeg-turbo-devel automake
gcc kernel-devel -y  
ENV PKG_CONFIG_PATH='/usr/local/lib/pkgconfig'  
ENV LD_LIBRARY_PATH='/usr/local/lib':$LD_LIBRARY_PATH  
  
RUN npm install -g canvas  
RUN npm install -g node-gyp  
RUN npm install -g fabric@1.7.14  
  
RUN cd /usr/local/lib/node_modules/canvas && node-gyp rebuild  
  

