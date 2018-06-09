FROM node:8.7.0  
  
RUN apt-get update \  
&& apt-get install -y \  
gconf-service \  
libasound2 \  
libatk1.0-0 \  
libc6 \  
libcairo2 \  
libcups2 \  
libdbus-1-3 \  
libexpat1 \  
libfontconfig1 \  
libgcc1 \  
libgconf-2-4 \  
libgdk-pixbuf2.0-0 \  
libglib2.0-0 \  
libgtk-3-0 \  
libnspr4 \  
libpango-1.0-0 \  
libpangocairo-1.0-0 \  
libstdc++6 \  
libx11-6 \  
libx11-xcb1 \  
libxcb1 \  
libxcomposite1 \  
libxcursor1 \  
libxdamage1 \  
libxext6 \  
libxfixes3 \  
libxi6 \  
libxrandr2 \  
libxrender1 \  
libxss1 \  
libxtst6 \  
ca-certificates \  
fonts-liberation \  
libappindicator1 \  
libnss3 \  
lsb-release \  
xdg-utils \  
wget \  
unzip  
  
RUN wget --no-check-certificate https://github.com/suttang/documentation-
printer-man/archive/master.tar.gz \  
&& tar -zxvf master.tar.gz \  
&& rm master.tar.gz \  
&& mv documentation-printer-man-master app \  
&& cd app/ \  
&& npm install --production  
  
RUN mkdir -p /usr/share/fonts/opentype/notoserif \  
&& cd /usr/share/fonts/opentype/notoserif \  
&& wget https://noto-website.storage.googleapis.com/pkgs/NotoSerifCJKjp-
hinted.zip \  
&& unzip NotoSerifCJKjp-hinted.zip \  
&& rm NotoSerifCJKjp-hinted.zip  
  
RUN mkdir -p /usr/share/fonts/opentype/notosans \  
&& cd /usr/share/fonts/opentype/notosans \  
&& wget https://noto-website.storage.googleapis.com/pkgs/NotoSansCJKjp-
hinted.zip \  
&& unzip NotoSansCJKjp-hinted.zip \  
&& rm NotoSansCJKjp-hinted.zip  
  
RUN fc-cache -fv  
  
WORKDIR /app  
CMD npm start  

