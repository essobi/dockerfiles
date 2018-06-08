FROM python:2.7  
MAINTAINER Anton Iskov <aiskov@jiss-software.com>  
  
# Install WKHTMLTO  
RUN wget -q
http://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.3/wkhtmltox-0.12.3_linux-
generic-amd64.tar.xz \  
&& tar -xJf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz \  
&& cp -R wkhtmltox/* /usr/ \  
&& rm -rf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz wkhtmltox  
  
# Install app  
ENV SERVICE_DIR /opt/rendering-service  
  
ADD . ${SERVICE_DIR}  
WORKDIR ${SERVICE_DIR}  
RUN python setup.py install  
  
# Run app  
CMD python server.py

