FROM gw000/keras:2.1.4-py3-th-cpu  
  
USER root  
WORKDIR /tmp  
  
# TA-Lib  
ADD https://astuteinternet.dl.sourceforge.net/project/ta-lib/ta-lib/0.4.0/ta-
lib-0.4.0-src.tar.gz .  
RUN tar -xvzf ta-lib-0.4.0-src.tar.gz && \  
cd ta-lib/ && \  
./configure --prefix=/usr && \  
make && \  
make install  
RUN rm -R ta-lib ta-lib-0.4.0-src.tar.gz  
  
# Python  
RUN pip3 install --no-cache-dir \  
ccxt \  
pandas \  
TA-Lib \  
flask \  
pymongo \  
dnspython  
  
COPY . /home/src  
  
RUN mkdir -p /home/history /.theano  
  
RUN rm -rf /home/src/.git* && \  
chown -R 1000 /home && \  
chgrp -R 0 /home && \  
chmod -R g+w /home  
  
RUN chown -R 1000 /.theano && \  
chgrp -R 0 /.theano && \  
chmod -R g+w /.theano  
  
USER 1000  
WORKDIR /home  
  
ENV HISTORY_PATH=/home/history \  
KERAS_BACKEND=theano \  
FLASK_APP=/home/src/main.py \  
LC_ALL=C.UTF-8 \  
LANG=C.UTF-8  
  
CMD flask run --host=0.0.0.0 --port=8080  

