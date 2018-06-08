FROM ubuntu:15.10  
MAINTAINER SatoShun <shun.sato1@gmail.com>  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV PYTHONIOENCODING UTF-8  
ENV PYTHON_PATH /usr/bin/python3  
  
USER root  
  
RUN apt-get clean && apt-get upgrade -y && apt-get update -y --fix-missing  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
python3 python3-dev python3-setuptools libpython3.4-stdlib
libpython3.4-minimal  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq \  
libatlas-base-dev libatlas-base-dev liblapack-dev gfortran build-essential gcc
\  
curl libcurl4-openssl-dev \  
pkg-config libpng-dev libfreetype6 libfreetype6-dev  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py  
  
RUN pip3 install matplotlib ipython ipykernel ipywidgets jupyter && \  
python3 -m ipykernel.kernelspec  
  
RUN mkdir -p -m 700 /root/.jupyter/ && \  
echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
ENV TINI_VERSION v0.6.0  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
RUN chmod +x /usr/bin/tini  
ENTRYPOINT ["/usr/bin/tini", "--"]  
  
EXPOSE 8888  
CMD ["jupyter", "notebook", "--port=8888", "--no-browser"]  

