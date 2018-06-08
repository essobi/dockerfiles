FROM ubuntu:16.04  
MAINTAINER Holger Joest <holger@joest.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu xenial main" \  
> /etc/apt/sources.list.d/deadsnakes.list \  
&& echo "deb http://ppa.launchpad.net/brightbox/ruby-ng/ubuntu xenial main" \  
> /etc/apt/sources.list.d/brightbox-ruby-ng-xenial.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DB82666C
F5DA5F09C3173AA6  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
automake build-essential ca-certificates etoolbox gcc gfortran git gnumeric \  
gsl-bin libblas-dev libfreetype6-dev libgsl0-dev libjpeg-dev liblapack-dev \  
libpng-dev libpq-dev libtool make mercurial pandoc pandoc-citeproc pkg-config
\  
python3.5 python3.5-dev ruby2.3 ruby2.3-dev ssh \  
texlive-latex-recommended texlive-luatex texlive-xetex wget wkhtmltopdf \  
&& ln -s python3.5 /usr/bin/python3 \  
&& apt-get autoremove \  
&& apt-get clean  
  
RUN cd /tmp \  
&& wget --quiet https://bootstrap.pypa.io/get-pip.py \  
&& python3 ./get-pip.py \  
&& rm -f ./get-pip.py  
  
RUN pip3 install -U virtualenv==15.1.0 \  
&& pip3 install -U numpy==1.11.2 \  
&& pip3 install -U scipy==0.18.1 \  
&& pip3 install -U scikit-learn==0.18.1  
  
RUN cd /tmp \  
&& wget --quiet
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0-cp34-cp34m-linux_x86_64.whl
\  
&& mv tensorflow-0.11.0-cp34-cp34m-linux_x86_64.whl
tensorflow-0.11.0-cp35-cp35m-linux_x86_64.whl \  
&& pip3 install -U ./tensorflow-0.11.0-cp35-cp35m-linux_x86_64.whl \  
&& rm -f ./tensorflow-0.11.0-cp35-cp35m-linux_x86_64.whl  
  
RUN pip3 install -U sympy==1.0 \  
&& pip3 install -U pandas==0.19.1 \  
&& pip3 install -U nltk==3.2.1 \  
&& pip3 install -U matplotlib==1.5.3 \  
&& pip3 install -U statsmodels==0.6.1 \  
&& pip3 install -U scikit-image==0.12.3 \  
&& pip3 install -U pexpect==3.3 \  
&& pip3 install -U pyqtgraph==0.9.10 \  
&& pip3 install -U docutils==0.12 \  
&& pip3 install -U six==1.10.0 \  
&& pip3 install -U xlrd==1.0.0 \  
&& pip3 install -U joblib==0.10.3 \  
&& pip3 install -U chardet==2.3.0 \  
&& pip3 install -U Bottlechest==0.7.1 \  
&& pip3 install -U ipython==5.1.0 \  
&& pip3 install -U jupyter==1.0.0 \  
&& pip3 install jupyter_client==4.4.0 \  
&& pip3 install bash_kernel==0.4.1 \  
&& python3 -m bash_kernel.install  
  
RUN pip3 install -U pyyaml==3.12 \  
&& pip3 install -U h5py==2.6.0 \  
&& pip3 install -U keras==1.1.2  
  
RUN pip3 install -U thrift==0.9.3 \  
&& pip3 install -U happybase==1.0.0  
  
RUN pip3 install xlsxwriter  
  
# TODO: spark mllib  
RUN cd /usr/local/lib/python3.5/dist-packages/notebook/static/components \  
&& wget --quiet https://github.com/mathjax/MathJax/archive/v2.6-latest.tar.gz
\  
&& rm -rf MathJax && tar xzf v2.6-latest.tar.gz && mv -f MathJax-2.6-latest
MathJax  
  
ENV LD_LIBRARY_PATH /var/lib/gems/2.3.0/gems/rbczmq-1.7.9/ext/rbczmq/dst/lib/  
RUN ln -s /usr/bin/libtoolize /usr/bin/libtool \  
&& gem install rbczmq -v 1.7.9 \  
&& gem install iruby -v 0.2.9  
  
RUN useradd notebook && mkdir /home/notebook /notebook \  
&& chown notebook /home/notebook /notebook  
USER notebook  
WORKDIR /notebook  
RUN iruby register  
  
RUN cd /tmp \  
&& git clone https://github.com/damianavila/RISE.git \  
&& cd RISE && git checkout 3.x.1 \  
&& python3 setup.py install  
  
EXPOSE 8888  
VOLUME [ "/notebook" ]  
  
CMD [ "sh", "-c", "jupyter notebook --no-browser --ip=0.0.0.0 --port=8888
--notebook-dir=/notebook" ]  

