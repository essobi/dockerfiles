FROM tsutomu7/scientific-python  
  
RUN conda install -y nltk redis redis-py && \  
pip install janome pymongo stop-words && \  
find /opt/conda/lib/python3.5 -name __pycache__ | xargs rm -r && \  
sudo rm -rf /opt/conda/pkgs/*  
EXPOSE 8888  
ADD data.tgz /home/scientist/  
CMD ["sh", "-c", "jupyter notebook --ip=*"]  

