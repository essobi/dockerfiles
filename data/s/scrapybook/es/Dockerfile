FROM scrapybook/base  
  
COPY scripts /tmp/scripts  
  
RUN /tmp/scripts/setup.sh  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
EXPOSE 9200 9300  

