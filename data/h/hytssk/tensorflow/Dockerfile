From tensorflow/tensorflow:latest  
MAINTAINER Hayato Sasaki <h.sasaki.ynu@gmail.com>  
# install openssh-server for ssh  
# install python-qt4 for matplotlib backend  
RUN apt-get update && \  
apt-get install -y openssh-server python-qt4 --no-install-recommends  
# upgrade pip  
RUN pip --no-cache-dir install --upgrade pip  
# install scikit-learn  
RUN pip --no-cache-dir install sklearn  
# add user 'developer'  
RUN adduser --disabled-password --gecos "" developer && \  
echo "developer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
echo "developer:developer" | chpasswd && \  
cp -r /notebooks /home/developer && chown -R developer:developer
/home/developer/notebooks && \  
cp -r /root/.jupyter /home/developer && chown -R developer:developer
/home/developer/.jupyter  
# edit /etc/ssh/sshd_config  
RUN sed -ri 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config && \  
sed -ri 's/^backend.*$/backend : Qt4agg/g' /usr/local/lib/python2.7/dist-
packages/matplotlib/mpl-data/matplotlibrc && \  
mkdir -p /var/run/sshd && \  
chmod 755 /var/run/sshd  
RUN echo "#!/usr/bin/env bash\\\n/usr/sbin/sshd\\\n/run_jupyter.sh" > /run.sh
&& chmod +x /run.sh  
# avoid AttributeError:NewBase is_abstract  
# https://github.com/tensorflow/tensorflow/issues/1965  
RUN echo "[global]\\\ntarget=/usr/lib/python2.7/dist-packages" > /etc/pip.conf
&& \  
pip install --no-cache-dir --upgrade six  
# remove apt related cache  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV QT_X11_NO_MITSHM 1  
USER developer  
WORKDIR /home/developer/notebooks  
CMD ["sudo", "/run.sh"]  

