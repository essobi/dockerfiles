#  
# Install ipython notebook to serve topfarm to a single user  
#  
FROM piredtu/topfarm  
  
MAINTAINER Pierre-Elouan Rethore <pire@dtu.dk>  
  
RUN apt-get install -y \  
ipython-notebook  
  
WORKDIR /install  
  
ADD requirements.txt /install/  
RUN pip install -r /install/requirements.txt  
  
ENV HOMEDIR /work  
RUN mkdir $HOMEDIR  
WORKDIR $HOMEDIR  
  
ADD install_kernels.sh /install/  
RUN chmod a+x /install/install_kernels.sh  
RUN /install/install_kernels.sh  
  
# Copying topfarm directory, and installing it in develop mode  
ADD install_topfarm_develop.sh /install/  
RUN chmod a+x /install/install_topfarm_develop.sh  
RUN /install/install_topfarm_develop.sh  
  
RUN ln -s /install $HOMEDIR/install  
  
EXPOSE 8888  
ENV PORT 8888  
RUN apt-get autoremove -y  
# Clear package repository cache  
RUN apt-get clean all  
  
ADD . /install  
RUN chmod a+x /install/run_notebook.sh  
  
WORKDIR $HOMEDIR  
CMD /install/run_notebook.sh  

