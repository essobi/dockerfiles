FROM debian:jessie  
  
RUN useradd -rM appuser \  
&& apt-get update \  
&& apt-get install -y \  
locales \  
nano \  
curl \  
libxrender1 \  
libfontconfig \  
libfreetype6 \  
libpng12-0 \  
libjpeg62-turbo \  
fontconfig \  
libxtst6 \  
xz-utils \  
xfonts-base \  
xfonts-75dpi \  
golang-go \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl
"https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-
amd64.tar.xz" -L -o "wkhtmltopdf.tar.xz"  
RUN tar Jxvf wkhtmltopdf.tar.xz  
RUN mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf  
  
# Ensure we can use UTF-8 characters like the copyright sign, in e.g. a PDF
header or footer.  
RUN sed -i 's/^# *\\(nl_BE.UTF-8\\)/\1/' /etc/locale.gen && locale-gen  
RUN echo "LANGUAGE=nl_BE.UTF-8" >> /etc/default/locale  
RUN echo "LANG=nl_BE.UTF-8" >> /etc/default/locale  
  
RUN mkdir /usr/share/fonts/truetype/wkhtmltopdf  
  
RUN mkdir /docker-fonts-initdb.d  
RUN mkdir /docker-resources-initdb.d  
  
COPY /app /usr/src/app  
  
RUN mkdir /app && \  
cd /usr/src/app && \  
go build -v -o /app/app  
  
WORKDIR /app  
EXPOSE 3000  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/app/app"]  

