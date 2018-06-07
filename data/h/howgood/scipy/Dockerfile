# howgood/scipy:jupyter  
FROM howgood/scipy:tools  
  
# Install tini to manage stray jupyter processes  
ENV TINI_VERSION v0.10.0  
RUN curl -L -o /tmp/tini \  
"https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini" \  
&& mv /tmp/tini /usr/local/bin/tini \  
&& chmod +x /usr/local/bin/tini  
  
# Install the ipython kernel spec, and run it. Then install
jupyter/ipynotebook  
RUN pip install --no-cache-dir --upgrade ipykernel \  
&& python -m ipykernel.kernelspec \  
&& pip install --no-cache-dir --upgrade \  
jupyter \  
ipython[notebook] \  
widgetsnbextension \  
&& rm -Rf ~/.cache ~/.local /tmp/*  
  
# Add default wildcard ip to jupyter config  
RUN mkdir -p -m 700 ~/.jupyter/ \  
&& echo "c.NotebookApp.ip = '*'" >> ~/.jupyter/jupyter_notebook_config.py  
  
# Add a notebooks volume, and default to that working directory  
ENV NOTEBOOK_DIR /usr/src/notebooks  
VOLUME ${NOTEBOOK_DIR}  
WORKDIR ${NOTEBOOK_DIR}  
  
EXPOSE 8888  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
CMD ["jupyter", "notebook", "--no-browser"]  

