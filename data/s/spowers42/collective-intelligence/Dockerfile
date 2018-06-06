FROM ubuntu  
MAINTAINER Scott Powers <spowers.42@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y python-dev python-pip vim libfreetype6-dev pkg-config \  
libsqlite3-dev libzmq3-dev  
  
RUN pip install ipython feedparser beautifulsoup4 pysqlite Pillow numpy  
RUN pip install matplotlib seaborn pyzmq jinja2  
  
VOLUME /collective-intelligence  
WORKDIR /collective-intelligence  
  
EXPOSE 8888  
CMD ipython notebook --no-browser --ip=0.0.0.0 --port 8888 --pylab=inline  

