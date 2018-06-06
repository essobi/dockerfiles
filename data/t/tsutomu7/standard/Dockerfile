FROM tsutomu7/scientific-python  
  
RUN pip install ortoolpy && \  
rm -rf $HOME/.c*  
EXPOSE 8888  
VOLUME $HOME  
COPY standard.tar.gz /tmp/  
CMD ["sh", "-c", "tar xf /tmp/standard.tar.gz && jupyter notebook --ip=*"]  

