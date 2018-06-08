FROM python:3.5  
COPY . /code  
WORKDIR /code  
RUN pip install -r requirements.txt  
ENTRYPOINT ["scrapy"]  
CMD ["crawl", "${SPIDER}"]

