FROM gcr.io/tensorflow/tensorflow:latest-py3  
WORKDIR /  
RUN \  
apt-get update &&\  
pip3 install jupyter &&\  
pip3 uninstall ipython -y &&\  
pip3 install ipython &&\  
pip3 install spacy &&\  
pip3 install pyLDAvis scipy nltk bokeh py4j &&\  
pip3 install -U scikit-learn &&\  
pip3 install keras &&\  
pip3 install numpy networkx gensim elasticsearch django pandas &&\  
pip3 install -U gensim &&\  
pip3 install pysal geojson hdbscan folium geopandas &&\  
apt-get clean &&\  
mkdir /opt/logs &&\  
touch start.sh &&\  
chmod 755 start.sh &&\  
echo "#!/bin/sh" >> start.sh &&\  
echo "nohup tensorboard --logdir=/data/logs > tb.out & nohup ./run_jupyter.sh
--allow-root>jupyter.out &" >> start.sh &&\  
echo "tail -f jupyter.out" >> start.sh  
RUN \  
python -m nltk.downloader all &&\  
python -m spacy download en  
EXPOSE 6006 8888  
CMD ["./start.sh"]

