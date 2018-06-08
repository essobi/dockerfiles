FROM pytorch/pytorch:latest  
  
RUN apt-get update && apt-get install -y \  
wget  
  
RUN pip install --upgrade pip  
RUN git clone https://github.com/moses-smt/mosesdecoder  
RUN git clone https://github.com/OpenNMT/OpenNMT-py.git && cd OpenNMT-py &&
pip install -r requirements.txt && python setup.py install  
RUN cd OpenNMT-py && wget
https://www.dropbox.com/s/06v7mn7b4u6l8dr/model_e13.pt  
  
RUN mkdir /data  
RUN mkdir /output  
  
RUN wget -O translate.sh
https://gist.github.com/ashatilov/9d414550bd23d775c96d6c168981ff72/raw  
RUN chmod a+x translate.sh  
  
CMD ["./translate.sh"]

