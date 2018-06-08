FROM ipoddaribm/powerai-examples  
  
ADD ./NAE/help.html /etc/NAE/help.html  
#WORKDIR /opt/DL  
#RUN wget https://s3.amazonaws.com/yb-lab-cfg/Tensorflow-Tutorials.tar.gz; tar
xvf Tensorflow-Tutorials.tar.gz; rm Tensorflow-Tutorials.tar.gz  
  
  
WORKDIR /root  
ADD startjupyter.sh /root/.startjupyter.sh  
ADD startjupyter_py3.sh /root/.startjupyter_py3.sh  
ADD startdigits.sh /root/.startdigits.sh  
ADD starttensorboard.sh /root/.starttensorboard.sh  
ADD starttftuts.sh /root/.starttftuts.sh  
ADD yb-sw-config.NIMBIX.ppc64le.mdt100.sh /root/sw-config.sh  
  
RUN chmod +x /root/.startjupyter.sh \  
&& chmod +x /root/.startjupyter_py3.sh \  
&& chmod +x /root/.startdigits.sh \  
&& chmod +x /root/.starttensorboard.sh \  
&& chmod +x /root/.starttftuts.sh \  
&& chmod +x /root/sw-config.sh  
  
ADD conf.d/* /etc/supervisor/conf.d/  
  
ADD ./install.tar /usr/local  
  
COPY ./.bashrc /etc/skel/.bashrc  
#add NIMBIX application  
COPY AppDef.json /etc/NAE/AppDef.json  
RUN curl \--fail -X POST -d @/etc/NAE/AppDef.json
https://api.jarvice.com/jarvice/validate  
  
RUN pip install -U scikit-learn \  
&& pip install -U prettytensor  
  
COPY ./jupyterhub_config.py /usr/local/jupyterhub_config.py  
  
RUN rm /root/startdigits.sh \  
&& rm /root/starttensorboard.sh \  
&& rm /root/startjupyter.sh  
  
WORKDIR /home/nimbix  
RUN /usr/bin/wget https://s3.amazonaws.com/yb-lab-
cfg/ibm-6.9.1.0-node-v6.9.1-linux-ppc64le.bin \  
&& /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/admin/yb-
admin.NIMBIX.ppc64le.tar \  
  
&& tar xvf yb-admin.NIMBIX.ppc64le.tar -C /usr/bin \  
&& sudo apt-get install -y tcl \  
&& sudo apt-get install -y git \  
  
&& echo 'export
PATH=/usr/local/node/bin:/usr/local/cuda/bin:/opt/ibm/xlC/13.1.5/bin:/opt/ibm/xlf/15.1.5/bin:$PATH'
>> .bashrc \  
&& echo 'export
PATH=/usr/local/node/bin:/usr/local/cuda/bin:/opt/ibm/xlC/13.1.5/bin:/opt/ibm/xlf/15.1.5/bin:$PATH'
>> /etc/bash.bashrc \  
&& export
PATH=/usr/local/node/bin:/usr/local/cuda/bin:/opt/ibm/xlC/13.1.5/bin:/opt/ibm/xlf/15.1.5/bin:$PATH
\  
  
&& sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/'
/etc/ssh/sshd_config \  
  
&& sudo service ssh restart \  
  
&& mkdir wetty \  
  
&& cd /home/nimbix/wetty \  
  
&& /usr/bin/yb-gencert yay \  
&& cd /home/nimbix \  
  
&& wget -q http://public.dhe.ibm.com/software/server/POWER/Linux/xl-
compiler/eval/ppc64le/ubuntu/public.gpg -O- | sudo apt-key add - \  
&& echo "deb http://public.dhe.ibm.com/software/server/POWER/Linux/xl-
compiler/eval/ppc64le/ubuntu/ trusty main" | sudo tee
/etc/apt/sources.list.d/ibm-xl-compiler-eval.list \  
&& sudo apt-get update \  
&& sudo apt-get install -y xlc.13.1.5 \  
&& sudo apt-get install -y xlf.15.1.5 \  
  
  
&& sudo apt-get update \  
&& sudo apt-get install -y apache2 mariadb-server libapache2-mod-php7.0 \  
&& sudo apt-get install -y php7.0-gd php7.0-json php7.0-mysql php7.0-curl
php7.0-mbstring \  
&& sudo apt-get install -y php7.0-intl php7.0-mcrypt php-imagick php7.0-xml
php7.0-zip \  
&& sudo a2enmod rewrite headers env dir mime setenvif ssl  
  
  
  
  
WORKDIR /  
RUN /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/ybcloud_v0.93.tar.gz \  
&& sudo tar xfpvz ybcloud_v0.93.tar.gz \  
  
&& /root/sw-config.sh \  
&& rm /root/sw-config.sh \  
&& echo 'export PATH=/root/anaconda2/envs/tensorflow/bin:$PATH' >>
/root/.bashrc \  
&& echo 'export PYTHONPATH=/root/anaconda2/envs/tensorflow/lib/python3.6/site-
packages/:$PYTHONPATH' >> /root/.bashrc \  
  
  
  
&& cd /root \  
&& wget https://github.com/google/prettytensor/archive/master.zip \  
&& unzip master.zip \  
&& rm master.zip \  
&& cd prettytensor-master \  
&& /root/anaconda2/bin/python setup.py install \  
  
&& /root/anaconda2/bin/pip install gym \  
&& /root/anaconda2/bin/pip install atari_py \  
&& pip install moldesign  
  
  
  
  
  
  
  

