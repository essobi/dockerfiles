FROM python:2  
RUN pip install --no-cache-dir \  
matplotlib requests boto multipledispatch prettytable \  
graphlab-create jupyter \  
&& jupyter notebook --generate-config \  
&& sed -i "s/#c.NotebookApp.ip = 'localhost'/c.NotebookApp.ip = '*'/g"
/root/.jupyter/jupyter_notebook_config.py  
  
ENV GRAPHLAB_KEY ""  
COPY entrypoint.sh /bin/entrypoint.sh  
  
ENTRYPOINT ["/bin/entrypoint.sh"]  
  
CMD ["jupyter", "notebook", "--allow-root"]  

