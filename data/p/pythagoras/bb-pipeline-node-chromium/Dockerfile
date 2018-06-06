FROM node:6.9.4  
  
# Install AWSCLI  
RUN apt-get update && \  
apt-get install -y \  
python3 \  
python3-pip \  
python3-setuptools \  
groff \  
less \  
&& pip3 install --upgrade pip \  
&& apt-get clean  
  
RUN pip3 --no-cache-dir install --upgrade awscli==1.14.38  
  
  
# Install Chromium  
RUN apt-get update && apt-get install -y xvfb chromium  
ADD xvfb-chromium /usr/bin/xvfb-chromium  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome && chmod +x
/usr/bin/google-chrome  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser && chmod +x
/usr/bin/chromium-browser  
ENV CHROME_BIN="/usr/bin/google-chrome"

