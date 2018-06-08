FROM ubuntu:14.04  
MAINTAINER Axel Oehmichen <axelfrancois.oehmichen11@imperial.ac.uk>  
  
WORKDIR /root  
  
ADD irkernel_install.r /root  
ADD start_eae.sh /root  
  
RUN apt-get update -q \  
&& apt-get upgrade -y --install-recommends \  
&& apt-get install -y vim wget git python-numpy python-scipy python-matplotlib
ipython python-pip python-scikits-learn nodejs-legacy npm zip
libcurl4-openssl-dev libxml2-dev screen openssh-server  
  
RUN pip install scimath \  
&& pip install pymongo \  
&& export
TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp27-none-
linux_x86_64.whl \  
&& sudo pip install --upgrade $TF_BINARY_URL \  
&& chmod 777 start_eae.sh \  
&& useradd -ms /bin/bash eae \  
&& mkdir /home/eae/.ssh \  
&& chmod 700 /home/eae/.ssh  
  
## Setting up Jupyter notebook and we create the folder where the jupyter
notebooks will run  
RUN pip install setuptools pip --upgrade --user \  
&& pip install ipython==5.2.1 \  
&& pip install jupyter \  
&& git clone https://github.com/aoehmichen/notebook.git \  
&& cd notebook \  
&& npm cache clean -f \  
&& npm install -g n \  
&& n stable \  
&& pip install -e . --user \  
&& cd /root \  
&& jupyter-nbextension enable \--py widgetsnbextension \  
&& mkdir -p /home/eae/jupyter \  
&& chown eae:eae /home/eae/jupyter \  
&& chmod 777 /home/eae/jupyter \  
&& cd /home/eae/jupyter  
  
## Setting up R and R Kernel  
RUN wget https://mran.revolutionanalytics.com/install/mro/3.3.1/microsoft-r-
open-3.3.1.tar.gz \  
&& tar xzf microsoft-r-open-3.3.1.tar.gz \  
&& cd microsoft-r-open \  
&& ./install.sh \  
&& cd /root \  
&& Rscript irkernel_install.r  
  
EXPOSE 22 7777  
VOLUME ["/root/jupyter/"]  
  
ENTRYPOINT ["bash", "/root/start_eae.sh"]  
  
## Default parameters in case the user does not provide them wih the RUN
commande  
CMD ["-deamon", interfaceeae, 8443, jupytereae, 22]

