# The MIT License (MIT)  
#  
# Copyright (c) 2016 CNRS  
#  
# Permission is hereby granted, free of charge, to any person obtaining a copy  
# of this software and associated documentation files (the "Software"), to
deal  
# in the Software without restriction, including without limitation the rights  
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
# copies of the Software, and to permit persons to whom the Software is  
# furnished to do so, subject to the following conditions:  
#  
# The above copyright notice and this permission notice shall be included in
all  
# copies or substantial portions of the Software.  
#  
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM,  
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE  
# SOFTWARE.  
#  
# AUTHORS  
# Hervé Bredin (bredin@limsi.fr)  
  
FROM pyannote/base-audiovisual  
MAINTAINER Hervé Bredin <bredin@limsi.fr>  
  
# -- Torch (deep learning) --  
  
RUN curl -s https://raw.githubusercontent.com/torch/ezinstall/master/install-
deps | bash -e && \  
git clone https://github.com/torch/distro.git ~/torch \--recursive && \  
cd ~/torch && \  
./install.sh && \  
~/torch/install/bin/luarocks install nn && \  
~/torch/install/bin/luarocks install dpnn && \  
~/torch/install/bin/luarocks install image && \  
~/torch/install/bin/luarocks install optim && \  
~/torch/install/bin/luarocks install csvigo  
  
ENV LD_LIBRARY_PATH /usr/local/lib:/opt/OpenBLAS/lib  
ENV PATH
~/torch/install/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  

