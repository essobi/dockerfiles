FROM python:2  
MAINTAINER FU YAO & LI YANZHE  
  
WORKDIR /usr/src/app  
  
ADD ./ ./ConSpider  
  
WORKDIR ConSpider  
  
RUN pip install -U pip \  
&& pip install -r requirements.txt  
  
CMD ["scrapy","crawl","contentSpider"]  

