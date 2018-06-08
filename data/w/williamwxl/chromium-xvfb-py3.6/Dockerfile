FROM python:3.6-jessie  
  
ENV CHROMEDRIVER_VERSION 2.36  
ENV CHROMEDRIVER_SHA256
2461384f541346bb882c997886f8976edc5a2e7559247c8642f599acd74c21d4  
  
ADD xvfb-chromium /usr/bin/xvfb-chromium  
  
RUN apt-get update && apt-get install -y \  
curl xvfb chromium unzip libgconf-2-4 && \  
ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome && \  
ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser && \  
curl -SLO
"https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
&& \  
echo "$CHROMEDRIVER_SHA256 chromedriver_linux64.zip" | sha256sum -c && \  
unzip "chromedriver_linux64.zip" -d /usr/local/bin && \  
rm "chromedriver_linux64.zip"  
  
WORKDIR /usr/src/app  
  

