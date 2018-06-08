FROM ubuntu:14.04  
MAINTAINER Alexander Sibiryakov <sibiryakov@scrapinghub.com>  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7  
RUN echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | tee
/etc/apt/sources.list.d/scrapy.list  
RUN apt-get update && apt-get install -y \  
scrapy \  
python-dev \  
python-pip  
  
ADD . /app  
  
RUN pip install -r /app/requirements.txt  
RUN python -m nltk.downloader punkt  
  
WORKDIR /app  
  
ENTRYPOINT ["/usr/bin/scrapy", "crawl", "score"]

