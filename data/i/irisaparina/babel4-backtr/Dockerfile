FROM strawberrypie/pytorch-cuda8:v0.3  
  
RUN git clone https://github.com/OpenNMT/OpenNMT-py.git && cd OpenNMT-py &&
pip install -r requirements.txt && python setup.py install  
RUN curl -s -L
https://raw.githubusercontent.com/saparina/babel4-backtr/master/run.sh?token=AVTxeELLDnOPVs0Xw_J-
DJ0c7kft3S7Pks5afKj6wA%3D%3D -o ~/run.sh && chmod +x ~/run.sh  
RUN curl -s -L
https://gist.github.com/strawberrypie/ba1f630f17d59f71862417565ceaa6f8/raw -o
~/split_parallel_corpus.py && chmod +x ~/split_parallel_corpus.py  
RUN curl -s -L
https://gist.githubusercontent.com/saparina/1a49645b40a20339a4aee7b2870946ff/raw/1e058a33fb772505ad2159b94827cb7ca032a323/shuffling_backtr.py
-o ~/shuffling.py && chmod +x ~/shuffling.py  

