# Author: Yale Huang  
#  
# Usage: nvidia-docker run -it -p 8888:8888 --cap-add SYS_ADMIN --device
/dev/fuse \  
# --security-opt apparmor=unconfined --name yale.huang.colaboratory \  
# yaleh/colaboratory-tensorflow \  
# /run_jupyter.sh --NotebookApp.token='' \  
# --NotebookApp.allow_origin='https://colab.research.google.com' \  
# --allow-root  
FROM tensorflow/tensorflow:1.8.0-gpu-py3  
  
MAINTAINER Yale Huang <calvino.huang@gmail.com>  
  
RUN pip3 install jupyter_http_over_ws  
RUN jupyter serverextension enable \--py jupyter_http_over_ws  
RUN pip3 install --upgrade --ignore-installed notebook  
RUN pip3 install keras  
RUN pip3 install jupyterlab  
  
COPY run_jupyter.sh /  
  
EXPOSE 8888/tcp  
  
CMD ["/run_jupyter.sh"]  
  

