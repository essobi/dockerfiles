FROM jupyterhub/jupyterhub-onbuild:0.8.1  
MAINTAINER Shogun Team <shogun-team@shogun-toolbox.org>  
ENV LANG C.UTF-8  
COPY templates /srv/jp_templates  
COPY cull_idle_servers.py /usr/bin/cull_idle_servers.py  
RUN /opt/conda/bin/pip install oauthenticator==0.7.1 marathonspawner==0.3.1
python-dateutil  

