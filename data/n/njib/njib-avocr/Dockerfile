FROM ubuntu:18.04  
  
# Install dependencies and setup service  
RUN apt-get update -y \  
&& apt-get install -y \  
gnupg \  
clamav \  
tesseract-ocr \  
unpaper \  
exactimage \  
imagemagick \  
poppler-utils \  
ghostscript \  
curl \  
pdfgrep \  
&& freshclam -d --checks=12 \  
&& freshclam \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*

