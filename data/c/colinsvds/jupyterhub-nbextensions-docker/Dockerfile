FROM jupyterhub/jupyterhub:latest  
  
  
RUN conda install -y notebook  
RUN openssl req -batch -x509 -nodes -days 365 -newkey rsa:1024 -keyout
jupyterhub.key -out jupyterhub.crt  
  
RUN apt-get -y update  
RUN apt-get -y install vim  
RUN apt-get -y install libglib2.0-0 libsm6 libxrender1 libfontconfig1  
RUN conda create -n py2 -y python=2 ipykernel anaconda ipython jsonschema
scipy notebook pandas matplotlib jupyter numpy scikit-learn seaborn  
RUN /bin/bash -c "source activate py2 && ipython kernel install --display-name
py2 --name py2 && source deactivate"  
RUN conda install anaconda ipython jsonschema scipy notebook pandas matplotlib
jupyter numpy scikit-learn seaborn  
RUN pip install psutil  
RUN pip install ipywidgets  
RUN git clone https://github.com/ipython-contrib/IPython-notebook-
extensions.git  
RUN IPython-notebook-extensions/setup.py install  
  
RUN adduser colin  
RUN echo "colin:svds" | chpasswd  
  
RUN echo "c.JupyterHub.admin_access = True\nc.Authenticator.admin_users =
{'colin'}\nc.JupyterHub.ssl_cert =
'/srv/jupyterhub/jupyterhub.crt'\nc.JupyterHub.ssl_key =
'/srv/jupyterhub/jupyterhub.key'" > /srv/jupyterhub/jupyterhub_config.py  
  
RUN mkdir /home/colin/.local  
RUN mkdir /home/colin/.local/share  
RUN mkdir /home/colin/.local/share/jupyter  
RUN cp -r /root/.local/share/jupyter/templates
/home/colin/.local/share/jupyter/templates  
RUN cp -r /root/.local/share/jupyter/extensions
/home/colin/.local/share/jupyter/extensions  
RUN cp -r /root/.local/share/jupyter/nbextensions
/home/colin/.local/share/jupyter/nbextensions  
RUN echo "from jupyter_core.paths import jupyter_config_dir,
jupyter_data_dir\nimport os.path\nimport
sys\n\nsys.path.append(os.path.join(jupyter_data_dir(), 'extensions'))\n\nc =
get_config()\n\nc.NotebookApp.extra_template_paths =
[os.path.join(jupyter_data_dir(), 'templates')
]\nc.NotebookApp.nbserver_extensions = {'nbextensions': True}\n" >
/root/.jupyter/jupyter_notebook_config.py  
  
RUN mkdir /home/colin/.jupyter  
RUN cp /root/.jupyter/jupyter_notebook_config.py
/home/colin/.jupyter/jupyter_notebook_config.py  
RUN cp /root/.jupyter/jupyter_notebook_config.json
/home/colin/.jupyter/jupyter_notebook_config.json  
RUN sed -i -e 's/root/home\/colin/g'
/home/colin/.jupyter/jupyter_notebook_config.json  
RUN mkdir /home/colin/.jupyter/nbconfig  
RUN echo "{\n \"load_extensions\": {\n \"config/config_menu/main\": true\n
}\n}" > /home/colin/.jupyter/nbconfig/notebook.json  
  
RUN chown -Rv colin /home/colin/

