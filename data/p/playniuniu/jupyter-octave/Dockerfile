FROM alpine:edge  
MAINTAINER playniuniu@gmail.com  
  
ENV PACKAGES curl python3 octave gnuplot ttf-opensans ghostscript  
ENV BUILD_ESSENTIAL make gcc g++ python3-dev  
ENV PIP_PACKAGE jupyter octave_kernel ipywidgets  
  
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add --no-cache --update ${PACKAGES} ${BUILD_ESSENTIAL} \  
&& python3 -m venv /env/ \  
&& /env/bin/pip install --upgrade pip \  
&& /env/bin/pip install ${PIP_PACKAGE} \  
&& /env/bin/python3 -m octave_kernel.install \  
&& /env/bin/jupyter nbextension enable \--py --sys-prefix widgetsnbextension \  
&& apk del ${BUILD_ESSENTIAL} \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /root/.cache/pip/*  
  
VOLUME /opt/  
EXPOSE 8888  
CMD ["/env/bin/jupyter", "notebook", "--allow-root"]  

