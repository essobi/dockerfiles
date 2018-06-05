# Fabre Dockerfile  
# https://github.com/Fiware/tools.Fabre  
#  
# Usage for HTML output:  
#  
# docker run -it --rm -v /home/login/project/doc/apib:/apib fiware/fabre -i
/apib/spec.apib -o /apib/html  
#  
# Usage for PDF output:  
#  
# docker run -it --rm -v /home/login/project/doc/apib:/apib fiware/fabre -i
/apib/spec.apib -o /apib/spec.pdf --pdf  
#  
FROM ubuntu:14.04  
ENV FABRE_VERSION 0.3.2  
RUN apt-get update -y && apt-get install -y unzip git python python-pip wget
build-essential  
RUN apt-get install -y libxml2-dev libxslt1-dev python-dev zlib1g-dev  
  
# Install drafter  
RUN git clone \--recursive --branch v0.1.9 --depth 1
git://github.com/FiwareULPGC/drafter.git && cd drafter && ./configure && make
drafter && make install && cd  
  
# Install Fabre  
RUN wget https://github.com/Fiware/tools.Fabre/archive/$FABRE_VERSION.zip &&
unzip $FABRE_VERSION.zip && cd tools.Fabre-$FABRE_VERSION && python setup.py
install && cd  
  
# Install wkhtmltopdf  
RUN apt-get install -y -f fontconfig libfontconfig1 libfreetype6 libjpeg-
turbo8 libxrender1 xfonts-base xfonts-75dpi  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
trusty-amd64.deb && dpkg -i wkhtmltox-0.12.2.1_linux-trusty-amd64.deb  
  
ENTRYPOINT ["fabre"]  

