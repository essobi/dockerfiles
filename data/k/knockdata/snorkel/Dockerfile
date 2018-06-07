FROM knockdata/python2  
  
RUN ls -alh /opt  
  
RUN conda install numba  
  
RUN jupyter nbextension enable \--py widgetsnbextension --sys-prefix  
  
RUN cd /opt/ \  
&& ls -alh /opt \  
&& git clone https://github.com/HazyResearch/snorkel.git \  
&& cd snorkel \  
&& git submodule update --init --recursive \  
&& ./install-parser.sh  
  
RUN cd /opt/snorkel/ \  
&& pip install -r python-package-requirement.txt  
  
RUN rm -rf /opt/snorkel/.git  
  
EXPOSE 8888  
CMD ["jupyter", "notebook", "--notebook-dir=/root/", "--ip='*'", "--
port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''"]

