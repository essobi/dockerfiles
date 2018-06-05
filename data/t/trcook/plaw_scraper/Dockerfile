FROM alpine:3.1  
#RUN echo
"http://nl.alpinelinux.org/alpine/edge/testing">>/etc/apk/repositories  
VOLUME /scrapy  
VOLUME /billsearch  
ADD ./billsearch/ /billsearch/  
ADD ./ /scrapy/  
  
CMD ["true"]  

