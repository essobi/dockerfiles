FROM ubuntu  
  
# Update the sources list  
RUN apt-get update  
  
# Install basic applications  
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
cmake  
  
# Install Python and Basic Python Tools  
RUN apt-get install -y python python-dev python-distribute python-pip  
  
RUN pip install gunicorn  
  
# Copy the application folder inside the container  
ADD /restfulgit /restfulgit  
  
ADD requirements.txt /requirements.txt  
  
RUN apt-get install -y libffi-dev # libgit2-dev  
  
RUN cd / ; wget -O libgit2.tar.gz
https://github.com/libgit2/libgit2/archive/v0.22.0.tar.gz; tar xf
libgit2.tar.gz ; rm libgit2.tar.gz ; cd libgit2-*; mkdir build && cd build ;
cmake .. -DCMAKE_INSTALL_PREFIX:PATH=/usr -DBUILD_CLAR=OFF && cmake --build .
; cmake --build . --target install ; cd / ; rm -rf libgit2-*  
  
# Get pip to download and install requirements:  
RUN pip install -r /requirements.txt  
  
ADD example_config.py /config.py  
  
RUN sed s#/Code/#/repos/# config.py -i ; sed 's#CORS = False#CORS = True#'
config.py -i  
  
VOLUME [/repos/]  
  
# Expose ports  
EXPOSE 5000  
WORKDIR /  
  
ENTRYPOINT PYTHONPATH=/ RESTFULGIT_CONFIG=/config.py python -m restfulgit.app

