# BUILD: docker build -t base .  
# RUN: docker run -it --rm -v (command pwd):/home/jochen/src/bitcoin bitcoin
/bin/sh  
# aws: sudo docker run -it --rm -v $PWD:/home/jochen/src/bitcoin -u 500
bitcoin /bin/sh  
#  
# aws:  
# sudo docker run -dt --name btc -v
/home/ec2-user/src/bitcoin:/home/jochen/src/bitcoin -u 500 gin66/bc_base
/bin/bash  
# sudo docker exec -it btc /usr/bin/tmux  
# => ./start.sh  
# sudo docker exec -it btc /usr/bin/tmux attach  
#  
#===========================================================================  
# This is from official docker python Dockerfile  
FROM gin66/bc_base:debian-base  
  
RUN pip3.6 install --upgrade setuptools  
RUN pip3.6 install six requests websocket-client requests-futures \  
pusherclient socketio_client pymemcache \  
numpy python-telegram-bot pypng scipy ipython \  
pika amqpstorm pillow h5py celery flower  
  
ENV TENSORFLOW_VERSION 1.2.0  
RUN pip3.6 --no-cache-dir install \  
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-${TENSORFLOW_VERSION}-cp36-cp36m-linux_x86_64.whl  
  
RUN pip3.6 install tflearn  
RUN pip3.6 install keras sqlite_object  
  
RUN /usr/sbin/adduser --disabled-login --uid 500 ec2-user  
RUN /usr/sbin/adduser --disabled-login --uid 1000 jochen  
RUN /usr/sbin/adduser --disabled-login --uid 5000 jo88ki88  
WORKDIR /home  
  

