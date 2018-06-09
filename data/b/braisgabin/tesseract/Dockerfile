FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
autoconf \  
automake \  
build-essential \  
ca-certificates \  
curl \  
git \  
libcairo2-dev \  
libicu-dev \  
libleptonica-dev \  
libpango1.0-dev \  
libpng12-dev \  
libtiff5-dev \  
libtool \  
zlib1g-dev \  
&& git clone --branch 3.04.01 --depth 1 https://github.com/tesseract-
ocr/tesseract.git /tmp/tesseract \  
&& cd /tmp/tesseract \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& make training \  
&& make training-install \  
&& ldconfig \  
&& cd / \  
&& curl -o /usr/local/share/tessdata/eng.traineddata \  
https://raw.githubusercontent.com/tesseract-
ocr/tessdata/master/eng.traineddata \  
&& apt-get purge --auto-remove -y \  
autoconf \  
automake \  
build-essential \  
ca-certificates \  
curl \  
git \  
libtool \  
&& apt-get clean \  
&& rm -rf /tmp/tesseract /var/lib/apt/lists/*  

