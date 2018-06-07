FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y sphinxsearch  
ADD config*.sh /  
RUN chmod +x config*.sh  
ADD indexer.sh /  
RUN chmod +x indexer.sh  
ADD searchd.sh /  
RUN chmod +x searchd.sh  
ADD sphinx.sh /  
RUN chmod +x sphinx.sh  
ADD writeconfig.sh /  
RUN chmod +x writeconfig.sh  
EXPOSE 9306 9312  
CMD ["/sphinx.sh"]  

