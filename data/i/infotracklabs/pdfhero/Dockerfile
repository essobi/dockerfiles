FROM microsoft/dotnet:2.0.5-sdk-2.1.4-jessie  
  
RUN mkdir /app  
WORKDIR /app  
  
# install node  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash \  
&& apt-get -y install nodejs  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
xz-utils \  
fontconfig \  
libfreetype6 \  
libx11-6 \  
libxext6 \  
libxrender1 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl
"https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-
amd64.tar.xz" \  
-L -o "wkhtmltopdf.tar.xz" \  
&& tar Jxvf wkhtmltopdf.tar.xz  

