# docker run --rm -u "$(id -u):$(id -g)" -v "$PWD":/usr/src/app -w
/usr/src/app mrjogo/scrapy  
FROM mrjogo/python  
MAINTAINER Ruddick Lawrence <mrjogo@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
gcc \  
libxml2-dev \  
libxslt1-dev \  
zlib1g-dev \  
libffi-dev \  
libssl-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install scrapy shub hubstorage  
  
CMD ["scrapy"]  

