FROM ruby:2.4.4  
ADD pgdg.list /etc/apt/sources.list.d/  
  
RUN wget -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add
- && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y postgresql-client-9.6 mysql-client sqlite3 --no-install-
recommends && \  
apt-get install -y build-essential imagemagick libmagic-dev nodejs-legacy xvfb
fontconfig libxfont1 xfonts-base xfonts-encodings xfonts-utils x11-common && \  
rm -rf /var/lib/apt/lists/*  
  
ENV WKHTMLTOPDF_DOWNLOAD_SHA256
049b2cdec9a8254f0ef8ac273afaf54f7e25459a273e27189591edc7d7cf29db  
RUN curl
"https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz" -L -o "wkhtmltopdf.tar.xz" && \  
echo "$WKHTMLTOPDF_DOWNLOAD_SHA256 *wkhtmltopdf.tar.xz" | sha256sum -c - && \  
tar Jxvf wkhtmltopdf.tar.xz && \  
mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf && \  
rm -rf wkhtmltox  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get install -y nodejs && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && \  
apt-get install -y yarn && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PHANTOMJS_DOWNLOAD_SHA256
86dd9a4bf4aee45f1a84c9f61cf1947c1d6dce9b9e8d2a907105da7852460d2f  
RUN curl
"https://github.com/Medium/phantomjs/releases/download/v2.1.1/phantomjs-2.1.1-linux-x86_64.tar.bz2"
-L -o "phantomjs.tar.bz2" && \  
echo "$PHANTOMJS_DOWNLOAD_SHA256 *phantomjs.tar.bz2" | sha256sum -c - && \  
tar xjf phantomjs.tar.bz2 && \  
mv phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs && \  
rm -rf phantomjs-2.1.1-linux-x86_64*  
  
ADD Gemfile* /app/  
WORKDIR /app  
RUN gem install bundler && gem cleanup && bundle install --full-index -j3  
  
EXPOSE 3000  
CMD ["rails", "server", "-b", "0.0.0.0"]  

