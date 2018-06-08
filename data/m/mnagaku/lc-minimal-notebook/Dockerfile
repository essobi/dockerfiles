FROM jupyter/base-notebook  
  
MAINTAINER mnagaku  
  
USER root  
  
# Copy config files  
ADD conf /tmp/  
  
RUN apt-get update && apt-get -yq upgrade && \  
apt-get install -yq \--no-install-recommends \  
git \  
vim \  
unzip \  
curl \  
iproute2 \  
fonts-ipafont-gothic fonts-ipafont-mincho && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
pip \--no-cache-dir install \--upgrade pip && \  
pip \--no-cache-dir install requests paramiko ansible pandas matplotlib pytz
folium papermill && \  
mkdir -p /etc/ansible && cp /tmp/ansible.cfg /etc/ansible/ansible.cfg && \  
cp /tmp/bash_env /etc/bash_env && \  
echo "$NB_USER ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/$NB_USER && \  
echo PATH=/opt/conda/bin:$PATH >> /root/.bash_profile && \  
sed -e "s/^Defaults.*secure_path.*\$//g" -i /etc/sudoers  
  
USER $NB_USER  
RUN mkdir -p $HOME/.jupyter && \  
cp -f /tmp/jupyter_notebook_config.py \  
$HOME/.jupyter/jupyter_notebook_config.py && \  
mkdir -p $HOME/.jupyter/nbconfig && \  
cp /tmp/notebook.json $HOME/.jupyter/nbconfig/notebook.json && \  
rm -rf ~/work  
  
USER root  
### extensions for jupyter (python3)  
#### jupyter_nbextensions_configurator  
#### jupyter_contrib_nbextensions  
#### nbextension_i18n (NII) - https://github.com/NII-cloud-
operation/Jupyter-i18n_cells  
#### Jupyter-LC_nblineage (NII) - https://github.com/NII-cloud-
operation/Jupyter-LC_nblineage  
#### Jupyter-LC_through (NII) - https://github.com/NII-cloud-
operation/Jupyter-LC_run_through  
#### Jupyter-LC_wrapper (NII) - https://github.com/NII-cloud-
operation/Jupyter-LC_wrapper  
#### Jupyter-multi_outputs (NII) - https://github.com/NII-cloud-
operation/Jupyter-multi_outputs  
#### Jupyter-LC_index (NII) - https://github.com/NII-cloud-operation/Jupyter-
LC_index  
RUN pip \--no-cache-dir install jupyter_nbextensions_configurator ipywidgets
six && \  
pip \--no-cache-dir install https://github.com/ipython-
contrib/jupyter_contrib_nbextensions/tarball/master && \  
pip \--no-cache-dir install git+https://github.com/NII-cloud-
operation/Jupyter-i18n_cells.git && \  
pip \--no-cache-dir install https://github.com/NII-cloud-operation/Jupyter-
LC_nblineage/tarball/master && \  
pip \--no-cache-dir install https://github.com/NII-cloud-operation/Jupyter-
LC_run_through/tarball/master && \  
pip \--no-cache-dir install https://github.com/NII-cloud-operation/Jupyter-
LC_wrapper/tarball/master && \  
pip \--no-cache-dir install git+https://github.com/NII-cloud-
operation/Jupyter-multi_outputs && \  
pip \--no-cache-dir install git+https://github.com/NII-cloud-
operation/Jupyter-LC_index.git  
  
  
USER $NB_USER  
RUN mkdir -p $HOME/.local/share && \  
jupyter contrib nbextension install \--user && \  
jupyter nbextension install \--py nbextension_i18n_cells \--user && \  
jupyter nbextension enable \--py nbextension_i18n_cells \--user && \  
jupyter run-through quick-setup \--user && \  
jupyter kernelspec install /tmp/kernels/python3-wrapper \--user && \  
jupyter nblineage quick-setup \--user && \  
jupyter nbextension enable \--user \--py widgetsnbextension && \  
jupyter nbextension install \--py lc_multi_outputs \--user && \  
jupyter nbextension enable \--py lc_multi_outputs \--user && \  
jupyter nbextension install \--py notebook_index \--user && \  
jupyter nbextension enable \--py notebook_index \--user && \  
mkdir -p $HOME/.jupyter/custom/ && \  
cp /tmp/custom.css $HOME/.jupyter/custom/custom.css && \  
cp /tmp/logo.png $HOME/.jupyter/custom/logo.png && \  
curl -fL
https://raw.githubusercontent.com/cytoscape/cytoscape.js/master/dist/cytoscape.min.js
> $HOME/.jupyter/custom/cytoscape.min.js && \  
curl -fL https://raw.githubusercontent.com/iVis-at-Bilkent/cytoscape.js-view-
utilities/master/cytoscape-view-utilities.js >
$HOME/.jupyter/custom/cytoscape-view-utilities.js && \  
curl -fL https://raw.githubusercontent.com/NII-cloud-operation/Jupyter-
LC_notebook_diff/master/html/jupyter-notebook-diff.js >
$HOME/.jupyter/custom/jupyter-notebook-diff.js && \  
curl -fL https://raw.githubusercontent.com/NII-cloud-operation/Jupyter-
LC_notebook_diff/master/html/jupyter-notebook-diff.css >
$HOME/.jupyter/custom/jupyter-notebook-diff.css && \  
mkdir -p $HOME/.ipython/profile_default/startup && \  
cp /tmp/10-custom-get_ipython_system.py
$HOME/.ipython/profile_default/startup/  
  
USER root  
SHELL ["/bin/bash", "-c"]  
CMD ["jupyter", "notebook"]  
### notebooks dir  
ADD sample-notebooks /home/$NB_USER  
RUN chown $NB_USER:users -R /home/$NB_USER  
  
USER $NB_USER  
ENV BASH_ENV=/etc/bash_env \  
SHELL=/bin/bash  

