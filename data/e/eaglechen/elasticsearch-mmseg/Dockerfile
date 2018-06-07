FROM java:8-jre  
MAINTAINER Eagle Chen <chygr1234@gmail.com>  
  
RUN cd /tmp && curl -OL https://github.com/medcl/elasticsearch-
rtf/archive/1.7.1.zip && \  
unzip 1.7.1.zip -d /usr/share && rm /tmp/1.7.1.zip && \  
mv /usr/share/elasticsearch-rtf-1.7.1 /usr/share/elasticsearch  
  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 9200 9300  
CMD ["elasticsearch"]  

