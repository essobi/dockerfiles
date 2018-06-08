From django:1.8.1-python2  
  
RUN apt-get update && apt-get install -y \  
python-zeroc-ice \  
python-imaging \  
python-simplejson \  
mercurial \  
python-pil \  
build-essential \  
python-dev \  
libjpeg-dev \  
libpng3 \  
libfreetype6-dev \  
libbz2-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install Pillow zeroc-ice  
RUN cd /usr/src && hg clone http://bitbucket.org/Svedrin/mumble-django && mv
mumble-django app  
RUN cd /usr/src/app && hg update stable  

