FROM python:3.6.4-slim-stretch  
  
RUN pip install jupyter  
RUN mkdir -p -m 700 /root/.jupyter/ && \  
echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py &&
\  
echo "c.NotebookApp.allow_root = True" >>
/root/.jupyter/jupyter_notebook_config.py && \  
echo "c.NotebookApp.open_browser = False" >>
/root/.jupyter/jupyter_notebook_config.py  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
CMD ["jupyter", "notebook"]

