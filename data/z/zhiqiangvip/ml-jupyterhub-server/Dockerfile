FROM jupyterhub/jupyterhub  
MAINTAINER qiang <zhiqiangvip999@gmail.com>  
  
# add default user  
RUN groupadd jupyterhub  
RUN useradd -g jupyterhub -m jupyter  
RUN echo "jupyter:123456" | chpasswd  
RUN pip install notebook  
  
# install numpy pandas  
RUN pip install matplotlib numpy pandas  
EXPOSE 8000  

