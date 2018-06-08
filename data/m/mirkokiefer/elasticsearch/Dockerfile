  
FROM mirkokiefer/java  
  
ADD install_es.sh /install_es.sh  
  
RUN bash /install_es.sh  
  
RUN echo 'export PATH=/elasticsearch/bin:$PATH' > $HOME/.bashrc  
  
EXPOSE 9200 9300  
CMD ["/elasticsearch/bin/elasticsearch"]  

