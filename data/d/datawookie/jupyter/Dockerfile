#
=============================================================================  
# JUPYTER NOTEBOOK DOCKER IMAGE  
#
=============================================================================  
  
# HTTPS
-----------------------------------------------------------------------  
  
# Ideally you should server JupyterHub over a secure (HTTPS) protocol.  
#  
# Here's what you need to do:  
#  
# 1\. Create a CNAME record in DNS which maps from your registered
(sub-)domain  
# to the host machine.  
#  
# 2\. Generate SSL certificates (https://letsencrypt.org/). You'll need to
have  
# these PEM files available:  
#  
# fullchain.pem - SSL certificate  
# privkey.pem - SSL key  
#  
# 3\. Uncomment the lines at the end of Dockerfile which copy the PEM files
onto  
# the image.  
#  
# 4\. In jupyterhub_config.py uncomment the following lines:  
#  
# c.JupyterHub.hub_port  
# c.JupyterHub.port  
# c.JupyterHub.ssl_cert  
# c.JupyterHub.ssl_key  
#  
# 5\. Build the image.  
#  
# 6\. Launch a container using -p 443:443.  
#  
# 7\. Make sure that the host accepts connections on port 443.  
#  
# 8\. Point your browser to the host.  
#  
# You might need to actually specify 'https://' in your browser so that it  
# looks for port 443.  
  
#
\-----------------------------------------------------------------------------  
#  
# A Jupyter Notebook with the following kernels:  
#  
# \- Python 3  
# \- Julia  
#  
# Currently the Julia kernel does not work. I think that this is because it's  
# installing Julia 0.3 and Jupyter requires Julia 0.4.  
#  
# Also note that the procedure below will install the Julia kernel in the  
# root user's home folder (~/.local/share/jupyter/kernels/). To make the Julia  
# kernel available to all users we will probably need to get it installed to  
# /usr/share/jupyter/kernels.  
#  
# To help with Julia:  
#  
# \- https://hub.docker.com/r/gnimuc/jupyterhub-docker-images/~/dockerfile/  
# \- https://github.com/felipenoris/math-server-docker/blob/master/Dockerfile  
#  
#
\-----------------------------------------------------------------------------  
#  
# To build:  
#  
# $ docker build -t jupyter:latest .  
#  
# To force a rebuild:  
#  
# $ docker build --no-cache -t jupyter:latest .  
#  
# To run:  
#  
# $ docker run -d -p 80:8000 jupyter:latest  
#  
#
\-----------------------------------------------------------------------------  
#  
FROM jupyterhub/jupyterhub:0.8.0b2  
MAINTAINER Andrew Collier <andrew@exegetic.biz>  
#  
# Install system software.  
#  
# \- build-essential: So that we can compile xgboost from source.  
#  
RUN apt-get update && \  
apt-get install -y \  
apg \  
build-essential \  
curl \  
git \  
locate \  
make \  
openssh-client \  
software-properties-common \  
unzip \  
vim \  
wget \  
whois && \  
apt-get clean -y  
  
#  
# RUN apt-get update && apt-get install -y julia  
# RUN apt-get update && apt-get dist-upgrade julia  
#  
# RUN add-apt-repository -y ppa:staticfloat/juliareleases  
# RUN apt-get update && apt-get install -y julia  
#  
# Install Julia packages.  
#  
# RUN julia -e 'Pkg.add("IJulia")'  
#  
# Install Python packages.  
#  
RUN pip install jupyter==1.0.0 \  
keras==2.0.6 \  
lightgbm==2.0.6 \  
matplotlib==2.0.2 \  
nltk==3.2.4 \  
numpy==1.13.1 \  
# orange3==3.4.5 \  
# orange3-associate==1.1.3 \  
pandas==0.20.3 \  
Pillow==4.2.1 \  
pytesseract==0.1.7 \  
scikit-learn==0.19.0 \  
scipy==0.19.1 \  
Scrapy==1.4.0 \  
statsmodels==0.8.0 \  
tensorflow==1.3.0 \  
theano==0.9.0 \  
xgboost==0.6a2  
#  
# Generate new user accounts.  
#  
# This is insecure and you should delete this user once everything is running.  
#  
RUN useradd jupyter -m -p `mkpasswd jupyter` -s /bin/bash  
  
# JupyterHub configuration file.  
#  
ADD jupyterhub_config.py /srv/jupyterhub/  
  
# Jupyter configuration file.  
#  
# Location of this file:  
#  
# \- $ jupyter --paths  
# \- http://jupyter.readthedocs.io/en/latest/projects/jupyter-
directories.html.  
#  
# Global location: /etc/jupyter/  
# Local location: ~/.jupyter/  
#  
# Custom settings:  
#  
# \- Automatically make copy of notebook as a plain .py script (enables
version control).  
#  
ADD jupyter_notebook_config.py /etc/jupyter/  
  
#  
# Set up SSL. (Uncomment the three lines below).  
#  
# ADD privkey.pem /etc/ssl/certs/privkey.pem  
# ADD fullchain.pem /etc/ssl/certs/fullchain.pem  
# RUN chmod 0600 /etc/ssl/certs/privkey.pem /etc/ssl/certs/fullchain.pem  
#  
# \- Currently using a self-signed certificate, but ultimately should use
letsencrypt.  
# \- In jupyterhub_config.py uncomment c.JupyterHub.ssl_cert and
c.JupyterHub.ssl_key.  
# \- Run with port mapping 443:8000.  
#  
# With the self-signed certificate you'll have to click on Advanced when you
visit the  
# site and choose to proceed (despite the dire consequences!). Your browser
will indicate  
# that the connection is not secure, but this just means that the certificate
can't be  
# validated. Communication is still happening via HTTPS.  
#  
# RUN apt-get install openssl  
# RUN mkdir /etc/certs/  
# RUN openssl req -x509 -nodes -days 730 -newkey rsa:2048 \  
# -subj "/C=US/ST=Washington/L=Seattle/O=Example Corporation/CN=example.com" \  
# -keyout /etc/certs/ssl.key -out /etc/certs/ssl.crt  

