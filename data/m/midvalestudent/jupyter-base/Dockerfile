FROM python:3.6  
# prereqs  
RUN DEBIAN_FRONTEND=noninteractive \  
&& REPO=http://cdn-fastly.deb.debian.org \  
&& echo "deb $REPO/debian jessie main\ndeb $REPO/debian-security
jessie/updates main" > /etc/apt/sources.list \  
&& apt-get update && apt-get -yq dist-upgrade \  
&& apt-get install -yq --no-install-recommends \  
wget \  
bzip2 \  
ca-certificates \  
sudo \  
locales \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# locale  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
locale-gen  
  
# Tini spawns a single child then cleans up any zombie processes before
exiting  
RUN wget --quiet
https://github.com/krallin/tini/releases/download/v0.14.0/tini \  
&& mv tini /usr/local/bin/tini \  
&& chmod +x /usr/local/bin/tini  
  
# packages  
ADD requirements.txt /usr/local/share/requirements.txt  
RUN pip install --upgrade pip && pip install -r
/usr/local/share/requirements.txt  
  
# notebook extensions  
RUN jupyter contrib nbextension install  
RUN jupyter nbextensions_configurator enable  
  
# create unprivileged user for running notebook  
ENV SHELL /bin/bash  
ENV NB_USER jovyan  
ENV NB_GROUP jovyan  
ENV HOME /home/$NB_USER  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
RUN groupadd $NB_GROUP && useradd -m -s $SHELL -g $NB_GROUP $NB_USER  
  
# set up the unpriviliged user's environment  
USER $NB_USER  
RUN mkdir /home/$NB_USER/.jupyter \  
&& mkdir -p -m 755 /home/$NB_USER/.local/share/jupyter \  
&& echo "cacert=/etc/ssl/certs/ca-certificates.crt" > /home/$NB_USER/.curlrc \  
&& umask 002  
ADD jupyter_notebook_config.py /home/$NB_USER/.jupyter/  
  
# back to root  
USER root  
ENV HOME /root  
  
# install startup scripts  
ADD start.sh /usr/local/bin/start.sh  
ADD start-notebook.sh /usr/local/bin/start-notebook.sh  
  
# default startup  
ENTRYPOINT ["tini", "--"]  
CMD ["start-notebook.sh"]  

