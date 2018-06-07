FROM fenicsproject/stable:latest  
MAINTAINER Jack S. Hale  
  
USER root  
  
RUN apt-get update && \  
apt-get install -yy pwgen npm nodejs-legacy python3-pip && \  
pip install --upgrade matplotlib && \  
npm install -g configurable-http-proxy && \  
pip3 install jupyterhub ipython[notebook] && \  
pip2 install --upgrade ipython[notebook]  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /usr/local/share/jupyter/kernels/python2  
COPY kernel.json /usr/local/share/jupyter/kernels/python2/kernel.json  
COPY jupyterhub_config.py /home/fenics/jupyterhub_config.py  
COPY make-users.sh /etc/my_init.d/make-users.sh  
RUN chmod +x /etc/my_init.d/make-users.sh  
  
USER fenics  
COPY fenics-matplotlib.py /home/fenics/fenics-matplotlib.py  
  
USER root  
ENV NUMBER_OF_USERS 10  
WORKDIR /home/fenics  
ENTRYPOINT ["/sbin/my_init","--"]  
CMD ["jupyterhub"]  

