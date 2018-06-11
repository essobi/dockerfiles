FROM yangzl/base-image:latest  
MAINTAINER YANG-ZL "zlyang65@gmail.com"  
RUN buildDeps='python3-dev python3-pip'; \  
set -x \  
&& apt-get update \  
&& apt-get install -y $buildDeps \  
&& pip3 install --upgrade pip \  
&& pip3 install jupyter \  
&& apt-get clean \  
&& jupyter notebook --generate-config \  
&& rm -rf /root/.jupyter/jupyter_notebook_config.py \  
&& mkdir -p /data/jupyternb \  
&& mkdir -p /data/Scripts \  
&& mkdir -p /root/.jupyter/custom  
  
COPY jupyter_notebook_config.py /root/.jupyter/jupyter_notebook_config.py  
COPY Scripts /data/Scripts/  
COPY custom /root/.jupyter/custom/  
RUN set -x \  
&& sed -Ei '2a jupyter notebook >> /var/log/jupyter.log 2>&1' /autoRun.sh  
ENTRYPOINT ["/autoRun.sh"]  
  
CMD ["/bin/bash"]  

