FROM mediadesignpractices/tensorflow:latest  
LABEL organization "Media Design Practices"  
LABEL maintainer "mediadesignpractices"  
LABEL contributor "unsalted"  
USER root  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
libhdf5-dev \  
python-dev \  
python3-h5py \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# change python version in mdp:latest  
ENV PYTHON_PIP_VERSION 9.0.1  
ENV PYTHON_VERSION $PYTHON3_VERSION  
  
# get pip3  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
# Below comes from pythons official docker release  
# explicit path to "pip3" to ensure distribution-provided "pip3" cannot
interfere  
RUN if [ ! -e /usr/local/bin/pip3 ]; then : \  
&& wget -O /tmp/get-pip.py 'https://bootstrap.pypa.io/get-pip.py' \  
&& python3 /tmp/get-pip.py "pip==$PYTHON_PIP_VERSION" \  
&& rm /tmp/get-pip.py \  
; fi \  
# we use "--force-reinstall" for the case where the version of pip we're
trying to install is the same as the version bundled with Python  
# ("Requirement already up-to-date: pip==8.1.2 in
/usr/local/lib/python3.6/site-packages")  
# https://github.com/docker-library/python/pull/143#issuecomment-241032683  
&& pip3 install \--no-cache-dir \--upgrade \--force-reinstall
"pip==$PYTHON_PIP_VERSION" \  
# then we use "pip list" to ensure we don't have more than one pip version
installed  
# https://github.com/docker-library/python/pull/100  
&& [ "$(pip list |tac|tac| awk -F '[ ()]+' '$1 == "pip" { print $2; exit }')"
= "$PYTHON_PIP_VERSION" ] \  
\  
&& find /usr/local -depth \  
\\( \  
\\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& rm -rf /usr/src/python ~/.cache  
  
# make some useful symlinks that are expected to exist  
RUN cd /usr/local/bin \  
&& { [ -e easy_install ] || ln -s easy_install-* easy_install; } \  
&& ln -s idle3 idle \  
&& ln -s pydoc3 pydoc \  
&& ln -s python3 python \  
&& ln -s python3-config python-config  
  
RUN pip3 \--no-cache-dir install \  
graphviz \  
pydot-ng \  
&& pip3 install git+git://github.com/Theano/Theano.git \  
&& pip3 install ipdb pytest pytest-cov python-coveralls coverage==3.7.1
pytest-xdist pep8 pytest-pep8 pydot_ng \  
&& pip3 install git+git://github.com/fchollet/keras.git  
  
WORKDIR /tmp  
  
RUN git clone https://github.com/fchollet/keras.git \  
&& mv ./keras/tests/ $HOME/ \  
&& rm -rf ./keras \  
&& chown $NB_USER $HOME  
ADD theanorc /home/keras/.theanorc  
  
USER $NB_USER  
WORKDIR $NOTEBOOK_DIR  
  
CMD ["/run_jupyter.sh"]  

