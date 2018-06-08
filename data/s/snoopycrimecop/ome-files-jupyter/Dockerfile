FROM openmicroscopy/ome-files-py:latest  
  
RUN pip install matplotlib jupyter  
RUN pip3 install matplotlib ipykernel  
RUN ipython3 kernel install  
  
EXPOSE 8888  
COPY run_jupyter /bin/  
RUN chmod +x /bin/run_jupyter  
  
RUN useradd -m jupyter  
USER jupyter  
ENV HOME /home/jupyter  
RUN mkdir -p -m 700 ${HOME}/.jupyter/ && \  
echo "c.NotebookApp.ip = '*'" >> ${HOME}/.jupyter/jupyter_notebook_config.py  
RUN mkdir -p -m 700 ${HOME}/notebooks  
COPY notebooks/*.ipynb ${HOME}/notebooks  
  
WORKDIR ${HOME}/notebooks  
  
RUN for kernel in python2 python3; do jupyter nbconvert
--ExecutePreprocessor.kernel_name="${kernel}" \--to notebook --execute
--stdout open_bytes.ipynb >/dev/null; done  
  
CMD ["run_jupyter"]  

