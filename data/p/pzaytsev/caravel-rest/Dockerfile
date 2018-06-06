FROM ubuntu:14.04  
MAINTAINER Pavel Zaytsev <zaytsev.pavel.a@gmail.com>  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
libssl-dev \  
libffi-dev \  
python-dev \  
python-pip \  
git \  
libmysqlclient-dev \  
libmysqlclient-dev && \  
apt-get build-dep -y psycopg2  
  
RUN pip install virtualenv  
RUN mkdir setup  
WORKDIR /setup  
RUN git clone https://github.com/PZaytsevUSC/ENV  
ENV VIRTUAL_ENV /setup/ENV/bin  
ENV PATH $VIRTUAL_ENV:$PATH  
RUN pip install mysqlclient==1.3.7  
WORKDIR /setup/ENV/lib/python2.7/site-packages  
  
ENV CARAVEL_HOME /setup/ENV/lib/python2.7/site-packages/caravel  
ENV CARAVEL_WEBSERVER_THREADS 8  
ENV PYTHONPATH $CARAVEL_HOME:$PYTHONPATH  
  
ENV ADMIN_USERNAME admin  
ENV ADMIN_FIRST_NAME admin  
ENV ADMIN_LAST_NAME user  
ENV ADMIN_EMAIL admin@nowhere.com  
ENV ADMIN_PWD caravel  
  
WORKDIR /  
ADD backend.sh /backend.sh  
RUN chmod a+x /backend.sh  
RUN ./backend.sh  
WORKDIR /setup/ENV/lib/python2.7/site-packages/caravel/assets  
  
RUN apt-get install wget  
ENV NVM_DIR /usr/local/nvm  
  
RUN wget -qO-
https://raw.githubusercontent.com/creationix/nvm/v0.31.2/install.sh | bash\  
&& source $NVM_DIR/nvm.sh\  
&& nvm install 6.2.0\  
&& nvm use 6.2.0  
  
ENV NODE_PATH $NVM_DIR/versions/node/v6.2.0  
ENV PATH $NODE_PATH/bin:$PATH  
  
RUN npm -v  
RUN npm cache clean  
RUN npm config set registry http://registry.npmjs.org/  
RUN npm config set strict-ssl false  
RUN npm install  
  
WORKDIR /setup/ENV/lib/python2.7/site-packages/caravel  
EXPOSE 8080  
CMD ["caravel", "runserver", "-p", "8080"]  

