FROM gforge/base-pytorch  
MAINTAINER Max Gordon <max@gforge.se>  
  
RUN apt-get update  
RUN apt-get install -y libgl1-mesa-glx  
  
RUN conda update conda  
RUN conda install -y \  
pandas \  
opencv \  
shapely \  
scikit-learn \  
matplotlib  
  
# Jupyter config  
RUN jupyter notebook --generate-config \  
&& printf "\nimport os\nfrom IPython.lib import passwd\npassword =
os.environ.get('JUPYTER_PASSWORD')\nif password:\n c.NotebookApp.password =
passwd(password)\n" \  
>> ~/.jupyter/jupyter_notebook_config.py  
  
# Expose Jupyter port  
EXPOSE 8888  
VOLUME /root  
WORKDIR /root  
  
RUN mkdir /models  
# Place to save the models using `torch.utils.model_zoo`  
RUN mkdir /models/zoo  
ENV TORCH_MODEL_ZOO /models/zoo  
  
# Where to mount the data  
RUN mkdir /data  
  
COPY resources /root  
# Change to for jupyter CMD ["/root/run_jupyter.sh"]  
CMD ["/bin/bash"]  
# python code/main.py -profile docker -datasets xray_full  

