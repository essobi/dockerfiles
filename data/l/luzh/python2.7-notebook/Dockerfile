# Python 2.7 with Jupyter Notebook (IPython Notebook)  
#  
# \--- Image Stack ---  
# luzh/python2.7-notebook  
# luzh/python2.7-imaging  
# luzh/python2.7-numerical  
# luzh/python2.7-baseline  
# luzh/centos7  
  
FROM luzh/python2.7-imaging  
  
# References:  
# http://jupyter.readthedocs.org/en/latest/install.html  
# https://hub.docker.com/r/ipython/notebook  
# https://github.com/ipython/docker-
notebook/blob/266cc06f7bcb348c6a0e0527fb4e593fe35387b9/notebook/Dockerfile  
  
RUN pip install --no-cache-dir jupyter  
  
VOLUME /notebook  
  
WORKDIR /notebook  
  
EXPOSE 8888  
  
ADD run.sh /  
  
# Let the docker container run it in background: PASSWORD=MakeAPassword
/run.sh &  
# CMD ["/run.sh"]  

