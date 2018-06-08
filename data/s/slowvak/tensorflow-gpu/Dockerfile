FROM gcr.io/tensorflow/tensorflow:latest-gpu  
MAINTAINER Bradley J Erickson <bje001@gmail.com>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -y update && apt-get install -y graphviz  
  
RUN pip install -U pip && pip --no-cache-dir install --upgrade \  
pandas \  
h5py \  
pyyaml \  
pycuda \  
scikit-learn \  
keras \  
seaborn \  
pydotplus  
  
# Set keras backend to tensorflow  
ENV KERAS_BACKEND tensorflow  
  
VOLUME /notebook  
WORKDIR /notebook  
  
# CMD ["/bin/bash"]  
# Add Tini. Tini operates as a process subreaper for jupyter. This prevents  
# kernel crashes.  
ENV TINI_VERSION v0.14.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/tini  
RUN chmod +x /tini  
ENTRYPOINT ["/tini", "--"]  
  
EXPOSE 8888  
CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--
allow-root"]  
  

