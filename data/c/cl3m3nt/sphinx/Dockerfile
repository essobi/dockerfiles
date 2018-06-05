FROM alpine:3.5  
LABEL maintainer "clement@le-corre.eu"  
LABEL description "Sphinx documentation tool"  
  
# Rewrite default value  
ENV SPHINX_DEFAULT_THEME sphinx_rtd_theme  
  
# Sphinx-quickstart default value  
ENV _SPHINX_DEFAULT_THEME alabaster  
  
RUN apk add --update --no-cache \  
python3 \  
py3-pip \  
make && \  
pip3 install --upgrade pip && \  
pip3 install sphinx sphinx_rtd_theme recommonmark  
  
RUN sed -i "s/${_SPHINX_DEFAULT_THEME}/${SPHINX_DEFAULT_THEME}/g" `find /
-name conf.py_t`  
  
VOLUME /root/docs  
WORKDIR /root/docs  
  
CMD ["/usr/bin/sphinx-quickstart"]  

