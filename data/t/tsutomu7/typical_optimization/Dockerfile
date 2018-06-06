FROM tsutomu7/scientific-python  
  
RUN pip install ortoolpy==0.2.1 && \  
rm -rf $HOME/.c*  
EXPOSE 8888  
VOLUME $HOME  
COPY typical.tgz /tmp/  
CMD ["sh", "-c", "tar xf /tmp/typical.tgz && jupyter notebook --ip=*"]  

