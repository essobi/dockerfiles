# based on kaixhin/mxnet, which is Ubuntu 14.04 based  
FROM kaixhin/mxnet:latest  
MAINTAINER Guo Quan <guoquanscu@gmail.com>  
  
# kaixhin/mxnet already installed: \  
# build-essential, git, libopenblas-dev, libopencv-dev, python-dev, python-
numpy, python-setuptools, wget  
# install ipython  
RUN apt-get update && apt-get install -y python-pip  
  
# install jupyter  
RUN pip install ipython jupyter  
  
# add Tini  
ENV TINI_VERSION v0.8.4  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
  
# expose 8888 as jupyter's default  
EXPOSE 8888  
# Set a seperated workspace as working directory  
WORKDIR /root/workspace  
  
# Optionally expose the workspace to the host  
VOLUME ["/root/workspace"]  
  
# Use tini to init the container  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
# Run notebook defaultly  
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser"]  

