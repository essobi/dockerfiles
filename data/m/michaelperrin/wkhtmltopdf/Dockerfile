FROM debian:jessie  
LABEL maintainer "Michaël Perrin <contact@michaelperrin.fr>"  
  
#docker run --rm -v `pwd`:/data my_wkhtmltopdf http://www.ecoguide-it.com/fr/  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
libxrender1 \  
libfontconfig \  
libxtst6 \  
xz-utils  
  
RUN curl
"https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-
amd64.tar.xz" -L -o "wkhtmltopdf.tar.xz"  
RUN tar Jxvf wkhtmltopdf.tar.xz  
RUN mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf  
  
ENTRYPOINT ["wkhtmltopdf"]  

