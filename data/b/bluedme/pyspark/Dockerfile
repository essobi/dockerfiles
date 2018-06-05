FROM bluedme/spark:1.6.0  
MAINTAINER bluedme  
  
RUN apt-get update && \  
apt-get install -y libncurses5-dev build-essential python3-dev python3-pip  
  
# python3-numpy python3-scipy python3-matplotlib  
RUN pip3 install jupyter plotly  
  
ENV
PYTHONPATH=$PYTHONPATH:/usr/local/spark/python/:/usr/local/spark/python/lib/py4j-0.9-src.zip  
ENV PYSPARK_PYTHON=/usr/bin/python3  
ENV PYSPARK_DRIVER_PYTHON=/usr/local/bin/ipython3  
  
  
# default command.  
CMD ["bash"]  

