# Copyright 2017  
# Permission is hereby granted, free of charge, to any person obtaining a copy
of this software  
# and associated documentation files (the "Software"), to deal in the Software
without  
# restriction, including without limitation the rights to use, copy, modify,
merge, publish,  
# distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom  
# the Software is furnished to do so, subject to the following conditions:  
# The above copyright notice and this permission notice shall be included in
all copies or  
# substantial portions of the Software.  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING  
# BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND  
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM,  
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING  
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.  
FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
build-essential \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python3 \  
python3-dev \  
rsync \  
software-properties-common \  
unzip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  
RUN pip \--no-cache-dir install \  
Pillow \  
h5py \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
pandas \  
scipy \  
sklearn \  
tensorflow \  
&& \  
python3 -m ipykernel.kernelspec  
  
RUN ln -s /usr/bin/python3 /usr/bin/python#  
# Set notebook config.  
COPY jupyter_config.py /root/.jupyter/  
# IPython  
EXPOSE 8888  
  
VOLUME /notebooks  
WORKDIR "/notebooks"  
CMD ["jupyter", "notebook", "--allow-root", "--NotebookApp.token="]  

