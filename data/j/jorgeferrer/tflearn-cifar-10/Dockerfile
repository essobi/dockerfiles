FROM tensorflow/tensorflow:0.11.0  
# GPUを利用師な場合は１行目をコメントアウトして代わりに下の行を有効にする  
# FROM tensorflow/tensorflow:nightly-gpu  
MAINTAINER Hayato Sasaki <h.developer.ynu@gmail.com>  
MAINTAINER Manuel de la Peña <manuel.delapenya@liferay.com>  
  
# set locale  
RUN locale-gen en_US.UTF-8  
RUN update-locale LANG=en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
ENV LC_ALL en_US.UTF-8  
ENV TERM xterm  
  
# git等のインストール  
RUN sed -i -r 's/\/\/archive.ubuntu.com/\/\/ftp.jaist.ac.jp/g'
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y git wget tree ca-certificates python-
qt4 --no-install-recommends  
  
# ユーザー'developer'を追加  
RUN adduser --disabled-password --gecos "" developer && \  
echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
echo "developer:developer" | chpasswd && \  
cp -r /root/.jupyter /home/developer && chown -R developer:developer
/home/developer/.jupyter  
RUN cp /run_jupyter.sh /home/developer/run_jupyter.sh && chown
developer:developer /home/developer/run_jupyter.sh  
# avoid AttributeError:NewBase is_abstract  
# https://github.com/tensorflow/tensorflow/issues/1965  
RUN echo "[global]\\\ntarget=/usr/lib/python2.7/dist-packages" > /etc/pip.conf
&& \  
pip install --no-cache-dir --upgrade six  
  
# jupyterのextensionsのインストール  
ENV JUPYTER_DATA_DIR /home/developer/.local/share/jupyter  
ENV JUPYTER_CONFIG_DIR /home/developer/.jupyter  
RUN pip --no-cache-dir install pyyaml && \  
pip --no-cache-dir install psutil && \  
pip --no-cache-dir install jupyter_nbextensions_configurator  
RUN git clone https://github.com/ipython-
contrib/jupyter_contrib_nbextensions.git jupyter_contrib_nbextensions && \  
cd jupyter_contrib_nbextensions && \  
python setup.py install && \  
cd .. && \  
rm -rf jupyter_contrib_nbextensions && \  
jupyter contrib nbextension install --user  
  
# chainerのインストール  
RUN pip install chainer --no-cache-dir  
  
# TFLearnのインストール  
RUN pip install --no-cache-dir h5py && pip install --no-cache-dir
git+https://github.com/tflearn/tflearn.git  
  
# pandasのインストール  
RUN pip install --no-cache-dir \  
cython \  
pandas  
  
# sklearn のインストール  
RUN pip install --no-cache-dir sklearn  
  
# キャッシュの削除  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# jupyterターミナルをshからbashへ変更  
RUN rm /bin/sh && \  
ln -s /bin/bash /bin/sh  
  
# matplotlibのbackendをQt4aggに変更  
RUN sed -ri 's/^backend.*$/backend : Qt4agg/g' /usr/local/lib/python2.7/dist-
packages/matplotlib/mpl-data/matplotlibrc  
ENV QT_X11_NO_MITSHM 1  
RUN chown -R developer:developer /home/developer/.local/share/jupyter  
RUN chown -R developer:developer /home/developer/.jupyter  
  
USER developer  
RUN mkdir /home/developer/notebooks  
COPY package_list.md /home/developer/notebooks/package_list.md  
#COPY full_dataset.pkl.zip /home/developer/notebooks/full_dataset.pkl.zip  
#COPY train-birds.ipynb /home/developer/notebooks/train-birds.ipynb  
COPY cifar-10.ipynb /home/developer/notebooks/cifar-10.ipynb  
WORKDIR /home/developer/notebooks  
  
CMD ["/home/developer/run_jupyter.sh"]  
  
RUN sudo chown -R developer:developer /home/developer/notebooks  

