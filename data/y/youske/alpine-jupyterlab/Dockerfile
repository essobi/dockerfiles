# Alpine Linux miniconda with Jupyterlab  
# youske/alpine-jupyter based  
FROM youske/alpine-jupyter:jupyter  
MAINTAINER youske miyakoshi <youske@gmail.com>  
  
LABEL com.geeplus.description="alpine jupyterlab image" \  
com.geeplus.role="jupyterlab baseimage"  
  
# jupyter lab  
RUN pip install jupyterlab && \  
jupyter serverextension enable \--py jupyterlab  
  
CMD ["gosu","admin","jupyter","lab","--no-browser", "--ip=*","--port=8888","--
notebook-dir=/workdir"]  

