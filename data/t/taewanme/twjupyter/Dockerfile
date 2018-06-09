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
RUN pip install --upgrade pip \  
&& python3 -m pip install --upgrade pip  
  
ENV TFPY3
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.0rc0-cp35-cp35m-linux_x86_64.whl  
RUN pip3 install --upgrade ${TFPY3}  
ENV TFPY
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.0rc0-cp27-none-
linux_x86_64.whl  
RUN pip install --upgrade ${TFPY3}  
  
RUN pip install numpy \  
&& pip install pillow \  
&& pip install matplotlib \  
&& pip install scikit-learn \  
&& pip install Pandas \  
&& pip install scrapy \  
&& pip install NLTK \  
&& pip install bokeh \  
&& pip install NetworkX \  
&& pip install --no-cache-dir scipy \  
&& pip install Seaborn \  
&& pip install xlrd  
  
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
&& pip install jupyter \  
&& pip3 install ipykernel \  
&& pip3 install beautifulsoup4  
  
COPY start-notebook.sh /usr/local/bin  
RUN chmod 755 /usr/local/bin/start-notebook.sh \  
&& chown -R taewan /usr/local/bin/start-notebook.sh  
  
RUN python3 -m ipykernel install --user  
  
RUN cp -rf /root/.local/share/jupyter/kernels/python3
/root/.local/share/jupyter/kernels/python2 \  
&& sed -i 's/python3/python/g'
/root/.local/share/jupyter/kernels/python2/kernel.json \  
&& sed -i 's/Python 3/Python 2/g'
/root/.local/share/jupyter/kernels/python2/kernel.json  
  
RUN mkdir -p /root/.jupyter/  
COPY jupyter_notebook_config.py /root/.jupyter/  
  
EXPOSE 8888  
VOLUME ["/home/taewan/ipython"]  
WORKDIR /home/taewan  
  
ENTRYPOINT ["/bin/bash", "start-notebook.sh"]

