# Docker file for building the smallest possible system user  
FROM ritjupyter/minimal-notebook  
MAINTAINER Joshua Milas <jgm6496@rit.edu>  
  
EXPOSE 8888  
USER root  
WORKDIR /home  
RUN userdel jovyan && rm -rf /home/jovyan  
ENV SHELL /bin/bash  
  
# Install python virtualenv  
RUN conda install --quiet --yes \  
'virtualenv=15.0.*' && \  
conda clean -tipsy  
  
# Get the single-user script  
RUN wget -q
https://raw.githubusercontent.com/jupyterhub/jupyterhub/0.6.1/scripts/jupyterhub-
singleuser -O /usr/local/bin/jupyterhub-singleuser && \  
chmod 755 /usr/local/bin/jupyterhub-singleuser  
  
# Get the systemuser script  
COPY systemuser.sh /srv/singleuser/systemuser.sh  
RUN chmod 755 /srv/singleuser/systemuser.sh  
  
# smoke test entrypoint  
RUN mkdir /home/systemusertest && USER_ID=65000 USER=systemusertest sh
/srv/singleuser/systemuser.sh -h && userdel systemusertest && rm -rf
/home/systemusertest  
  
CMD ["sh", "/srv/singleuser/systemuser.sh"]  

