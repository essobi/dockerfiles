FROM ubuntu:16.04  
MAINTAINER Taewan Kim <taewanme@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y curl apt-utils git make build-essential \  
libssl-dev libffi-dev zlib1g-dev libbz2-dev libreadline-dev \  
libsqlite3-dev python-pip python3-pip libjpeg8-dev python-dev \  
language-pack-ko python3-dev libxml2 libxml2-dev libxslt1-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# set locale ko_KR  
RUN locale-gen ko_KR.UTF-8  
ENV LANG ko_KR.UTF-8  
ENV LANGUAGE ko_KR.UTF-8  
ENV LC_ALL ko_KR.UTF-8  
RUN python3 -m pip install --upgrade pip  
  
RUN pip3 install xlrd \  
&& pip3 install numpy \  
&& pip3 install pillow \  
&& pip3 install matplotlib \  
&& pip3 install scikit-learn \  
&& pip3 install Pandas \  
&& pip3 install scrapy \  
&& pip3 install NLTK \  
&& pip3 install bokeh \  
&& pip3 install NetworkX \  
&& pip3 install scipy \  
&& pip3 install Seaborn \  
&& pip3 install jupyter \  
&& pip3 install beautifulsoup4 \  
&& pip3 install keras \  
&& pip3 install
http://download.pytorch.org/whl/cpu/torch-0.3.1-cp35-cp35m-linux_x86_64.whl \  
&& pip3 install torchvision \  
&& pip3 install --upgrade tensorflow  
  
RUN mkdir -p /root/.jupyter/  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
COPY start-notebook.sh /usr/local/bin  
  
EXPOSE 8888  
EXPOSE 6006  
VOLUME ["/root/ipython"]  
WORKDIR /root  
  
ENTRYPOINT ["/bin/bash", "start-notebook.sh"]  

