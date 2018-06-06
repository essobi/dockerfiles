FROM ubuntu:14.04  
MAINTAINER "Kazuhiko Kobayashi <kkoba84@gmail.com>"  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y build-essential  
RUN apt-get install -y python \  
python-dev \  
python-pip \  
python-zmq  
RUN apt-get install -y libhdf5-dev \  
libreadline-dev  
RUN apt-get install -y python-matplotlib ipython-notebook  
RUN apt-get install -y python-opencv  
RUN apt-get install -y git  
  
# upgrade setuptools  
RUN pip install -U setuptools  
  
# install cython  
RUN pip install -U cython  
  
# install hdf5  
RUN pip install -U h5py  
  
# install protocol buffer  
RUN pip install -U protobuf  
  
# install chainer  
RUN pip install -U chainer  
  
# upgrade ipython to jupyter  
RUN pip install -U "ipython[notebook]"  
RUN jupyter notebook --generate-config  
  
RUN echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py  
RUN echo "c.NotebookApp.open_browser = False" >>
/root/.jupyter/jupyter_notebook_config.py  
RUN echo "c.NotebookApp.port = 8000" >>
/root/.jupyter/jupyter_notebook_config.py  
  
RUN git clone https://github.com/pfnet/chainer.git /root/chainer --recursive  
  
WORKDIR /root/chainer  
VOLUME ["/root/chainer/local"]  
EXPOSE 8000  
ENTRYPOINT /usr/local/bin/jupyter notebook  
  

