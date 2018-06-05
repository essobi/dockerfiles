FROM alfakini/python-anaconda  
MAINTAINER Alan Fachini <alfakini@gmail.com>  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV PYTHONIOENCODING UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN conda update --all && \  
conda install --yes \  
jupyter \  
ipywidgets \  
scikit-learn \  
scikit-image  
  
RUN pip install widgetsnbextension && \  
jupyter nbextension enable \--py widgetsnbextension  
  
ADD configs/ /tmp/  
RUN mkdir -p -m 700 /root/.jupyter/ && \  
cp /tmp/jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py  
  
VOLUME /notebooks  
WORKDIR /notebooks  
EXPOSE 8888  
RUN apt-get -y update && \  
apt-get -y install \  
libatlas-base-dev \  
libjasper-dev \  
libgtk2.0-dev \  
libavcodec-dev \  
libavformat-dev \  
libswscale-dev \  
libjpeg-dev \  
libpng-dev \  
libtiff-dev \  
libjasper-dev \  
libv4l-dev \  
libopencv-dev  
  
ENV OPENCV_VERSION 3.1.0  
RUN conda install -c menpo --yes opencv3=${OPENCV_VERSION}  
  
ENV TINI_VERSION v0.9.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
CMD ["jupyter", "notebook", "--no-browser"]  
  

