FROM ircsphere/hyperstream:0.3.7  
MAINTAINER Kacper Sokol <ks1591@bristol.ac.uk>  
  
USER root  
RUN apt-get install -y python-numpy  
USER $HYPERSTREAM_USER  
  
#RUN git config --global user.email "docker@docker" &&\  
#git config --global user.name "Docker"  
RUN pip install --upgrade pip &&\  
pip install --user ipython[all] jupyter &&\  
pip install --user watermark  
  
# RUN git fetch origin tutorials:tutorials &&\  
# git stash &&\  
# git checkout tutorials &&\  
# git stash apply  
# Configure mongo connection  
RUN sed -i -e 's/localhost/hyperstream-mongo/g'
examples/hyperstream_config.json  
  
# Configure MQTT connection  
# RUN sed -i -e 's/mqtt_ip = "127.0.0.1"/mqtt_ip = "hyperstream-mqtt"/g'
tests/helpers.py  
# Start Jupyter Notebook  
EXPOSE 8888  
ENTRYPOINT jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --notebook-
dir=./examples  

