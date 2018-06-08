FROM debian:8  
RUN apt update && \  
apt install -y curl fontconfig libfreetype6 libx11-6 \  
libxext6 libxrender1 zlibc xz-utils && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /wk  
  
RUN curl -L -o wk.tar.xz \  
http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-
generic-amd64.tar.xz && \  
tar xf wk.tar.xz && \  
rm wk.tar.xz  
  
RUN cd /wk/wkhtmltox/bin && \  
ln -s $PWD/wkhtmltopdf /bin/wkhtmltopdf && \  
ln -s $PWD/wkhtmltoimage /bin/wkhtmltoimage  
  
USER 1000  
WORKDIR /code  

