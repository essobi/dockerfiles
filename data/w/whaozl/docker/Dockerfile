FROM nvidia/cuda:8.0-cudnn5-devel  
MAINTAINER whaozl <whaozl@163.com>  
  
RUN apt-get update && apt-get install -y \  
git \  
libopenblas-dev \  
libopencv-dev \  
python-dev \  
python-numpy \  
python-setuptools \  
wget \  
vim \  
openssh-server  
  
#vim support for chinese  
RUN echo "set fileencodings=utf-8,gb2312,gbk,gb18030\  
\nset termencoding=utf-8\  
\nset encoding=prc"\  
>> /etc/vim/vimrc  
  
  
# install pip  
RUN wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate \  
&& python get-pip.py \  
&& ln -s /usr/local/bin/pip /usr/bin/pip  
  
#install python lib  
RUN pip --no-cache-dir install wheel pillow nose scipy matplotlib
opencv_python protobuf \  
scikit-learn scikit-image pyyaml h5py pandas SimpleITK regex jieba openpyxl
xlsxwriter xlrd py_linq tqdm  
  
#install jupyter and jupyter lab and config jupyter  
#you should set password by  
#ipython  
#from notebook.auth import passwd  
#passwd() passwd default is 123456  
RUN pip --no-cache-dir install jupyter jupyterlab \  
&& jupyter serverextension enable --py jupyterlab --sys-prefix \  
&& jupyter notebook --generate-config --allow-root \  
&& echo "c.NotebookApp.ip='*'\n\  
c.NotebookApp.password=u'sha1:7de7ea9c4921:c5633014d406ce2f7cfa9a80b2be1c280fd9f42f'\n\  
c.NotebookApp.open_browser=False\n\  
c.NotebookApp.port=8888" \  
> /root/.jupyter/jupyter_notebook_config.py  
  
#install dl framework  
RUN pip --no-cache-dir install mxnet-cu80 tensorflow-gpu theano keras  
  
#config keras  
RUN mkdir /root/.keras && \  
echo '{\n \  
\n"image_dim_ordering": "tf", \  
\n"epsilon": 1e-07, \  
\n"floatx": "float32", \  
\n"backend": "tensorflow" \  
\n}' \  
> /root/.keras/keras.json  
  
#config theano  
RUN echo "[global] \  
\nopenmp=False \  
\ndevice=gpu \  
\noptimizer=fast_compile \  
\nfloatX=float32 \  
\noptimizer_including=cudnn \  
\nallow_input_downcast=True \  
\n[lib] \  
\ncnmem=0.8 \  
\n[blas] \  
\nldflags= -lopenblas \  
\n[nvcc] \  
\nfastmath=True" \  
> /root/.theanorc  
  
#config openssh-server ssh  
RUN cd /etc/ssh && \  
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/g' sshd_config
&& \  
sed -i 's/#PasswordAuthentication/PasswordAuthentication/g' sshd_config && \  
sed -i 's/RhostsRSAAuthentication no/RhostsRSAAuthentication yes/g'
sshd_config && \  
sed -i 's/HostbasedAuthentication no/HostbasedAuthentication yes/g'
sshd_config && \  
sed -i 's/PermitEmptyPasswords no/PermitEmptyPasswords yes/g' sshd_config && \  
sed -i 's/#KerberosAuthentication no/KerberosAuthentication yes/g' sshd_config
&& \  
sed -i 's/#KerberosOrLocalPasswd/KerberosOrLocalPasswd/g' sshd_config && \  
sed -i 's/#KerberosTicketCleanup/KerberosTicketCleanup/g' sshd_config  
  
RUN pip --no-cache-dir install
https://cntk.ai/PythonWheel/GPU/cntk-2.2-cp27-cp27mu-linux_x86_64.whl  
  
#CMD ln /dev/null /dev/raw1394  
#CMD ["sh", "-c", "ln /dev/null /dev/raw1394 ; /etc/init.d/ssh start ; nohup
jupyter lab >/dev/null 2>&1 &"]  
  
COPY start.sh /root/start.sh  
CMD sh /root/start.sh  
  
WORKDIR /

