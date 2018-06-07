FROM inklusive/rails  
  
USER root  
  
# libicu-dev: for charlock_holmes gem  
# tidy: to clean up bad html comming from printers and causing trouble parsing
due to inconsistencies  
# wicked pdf dependencies: fontconfig libfontconfig1 libfreetype6 libjpeg-
turbo8 libxrender1 xfonts-base xfonts-75dpi  
# imagemagick: image uploading  
# poppler-utils: pdftotext for bills analyser  
# libpq-dev: pg gem  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
libicu-dev tidy \  
imagemagick \  
poppler-utils \  
fontconfig \  
libfontconfig1 \  
libfreetype6 \  
libjpeg-turbo8 \  
libxrender1 \  
libpq-dev \  
xfonts-base \  
xfonts-75dpi  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN wget
'http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
precise-amd64.deb' -O /tmp/wkhtmltopdf.deb && dpkg -i /tmp/wkhtmltopdf.deb  
  
RUN rm /tmp/wkhtmltopdf.deb  
  
WORKDIR /app/erp_inklusive  
USER app  

