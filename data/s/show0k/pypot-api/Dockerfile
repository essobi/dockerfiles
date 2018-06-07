FROM show0k/alpine-miniconda  
MAINTAINER Théo Segonds <theo.segonds@inria.fr>  
  
  
USER root  
ADD patched_pypot /home/$NB_USER/pypot  
RUN chown -R $NB_USER /home/$NB_USER/pypot  
  
USER jovyan  
  
# Install Python 3 packages  
RUN conda install --yes scipy \  
&& conda clean -yt  
  
# Install custom pypot  
RUN cd /home/$NB_USER/pypot && \  
python setup.py install  
  
RUN pip install poppy-ergo-jr  
  
USER root  
  
# Pypot Snap API  
EXPOSE 6969  
EXPOSE 8080  
CMD [ "start-api.sh" ]  
  
COPY start-api.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/start-api.sh  
  
# Switch back to jovyan to avoid accidental container runs as root  
USER jovyan  

