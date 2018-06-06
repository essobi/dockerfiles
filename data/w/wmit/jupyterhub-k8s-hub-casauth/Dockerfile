FROM jupyterhub/k8s-hub:v0.6  
USER root  
RUN pip3 install wheel lxml && \  
pip3 install
git+https://github.com/cwaldbieser/jhub_cas_authenticator.git#egg=jhub_cas_authenticator  
USER jovyan  

