FROM ubuntu:14.04  
RUN echo "nameserver 172.17.42.1" > /etc/resolv.conf  
RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf  
RUN apt-get update  
RUN apt-get install -y python3-all-dev curl wget  
RUN ln -s /usr/bin/python3 /usr/bin/python  
RUN wget -qO- https://bootstrap.pypa.io/get-pip.py | python  
RUN wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
-P /tmp/  
RUN bash /tmp/Miniconda3-latest-Linux-x86_64.sh -b -p /opt/miniconda3  
RUN yes | pip install virtualenv  
RUN yes | /opt/miniconda3/bin/conda create -n ml_env numpy scipy scikit-learn
matplotlib cython ipython ipython-notebook  
RUN rm /tmp/Miniconda3-latest-Linux-x86_64.sh  
RUN apt-get autoremove -y  
RUN apt-get clean all  
RUN echo '# !/bin/bash' | sudo tee -a /etc/profile.d/conda.sh  
RUN echo 'export PATH="/opt/miniconda3/bin:${PATH}"' | sudo tee -a
/etc/profile.d/conda.sh  
RUN chmod 750 /etc/profile.d/conda.sh  

