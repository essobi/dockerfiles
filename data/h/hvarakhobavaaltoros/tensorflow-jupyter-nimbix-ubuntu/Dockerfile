FROM nimbix/ubuntu-base:trusty  
MAINTAINER hvarakhobava  
  
# recreate nimbix user home to get the right skeleton files  
RUN /bin/rm -rf /home/nimbix && /sbin/mkhomedir_helper nimbix  
  
# install python libs including tensorflow, jupyter  
RUN mkdir -p /etc/runtimescripts  
ADD deploy.sh /etc/runtimescripts/deploy.sh  
RUN chmod +x /etc/runtimescripts/deploy.sh && /etc/runtimescripts/deploy.sh  
  
EXPOSE 5901  
EXPOSE 443  
WORKDIR "/home/nimbix"  
  
# Set up our notebook config.  
COPY jupyter_notebook_config.py /root/.jupyter/  
RUN mkdir /root/.jupyter/notebooks  
RUN chmod +x /root/.jupyter/jupyter_notebook_config.py  
  
# Copy sample notebooks.  
# RUN mkdir -p .jupyter/notebooks  
# COPY notebooks .jupyter/notebooks  
# Jupyter has issues with being run directly:  
# https://github.com/ipython/ipython/issues/7062  
# We just add a little wrapper script.  
COPY run_jupyter.sh /  
RUN chmod +x /run_jupyter.sh  
  
# TensorBoard  
EXPOSE 6006  
# IPython  
EXPOSE 8888  
# Set the URL to the Tensorboard portal  
RUN mkdir -p /etc/NAE  
COPY ./NAE/url.txt /etc/NAE/url.txt  
COPY ./NAE/AppDef.json /etc/NAE/AppDef.json  
COPY ./NAE/AppDef.png /etc/NAE/AppDef.png  
  
COPY ./scripts/start.sh /etc/scripts/start.sh  
RUN chmod +x /etc/scripts/start.sh  

