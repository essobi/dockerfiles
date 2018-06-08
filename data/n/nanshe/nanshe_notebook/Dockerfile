FROM nanshe/nanshe:sge  
MAINTAINER John Kirkham <jakirkham@gmail.com>  
  
RUN for PYTHON_VERSION in 2 3; do \  
mkdir -p /notebooks && \  
export INSTALL_CONDA_PATH="/opt/conda${PYTHON_VERSION}" && \  
. "${INSTALL_CONDA_PATH}/etc/profile.d/conda.sh" && \  
conda activate base && \  
conda install -qy notebook && \  
conda install -qy ipywidgets && \  
conda install -qy jupyter_contrib_nbextensions && \  
conda install -qy nbconvert && \  
conda clean -tipsy && \  
conda deactivate && \  
python${PYTHON_VERSION} -m ipykernel install --name "python${PYTHON_VERSION}"
\--prefix "/opt/conda2" && \  
sed -i
"s/\/opt\/conda${PYTHON_VERSION}\/bin\/python/\/usr\/local\/bin\/python${PYTHON_VERSION}/g"
\  
"/opt/conda2/share/jupyter/kernels/python${PYTHON_VERSION}/kernel.json" && \  
python${PYTHON_VERSION} -m ipykernel install --name "python${PYTHON_VERSION}"
\--prefix "/opt/conda3" && \  
sed -i
"s/\/opt\/conda${PYTHON_VERSION}\/bin\/python/\/usr\/local\/bin\/python${PYTHON_VERSION}/g"
\  
"/opt/conda3/share/jupyter/kernels/python${PYTHON_VERSION}/kernel.json" && \  
rm -rf ~/.conda ; \  
done  
  
ENTRYPOINT [ "/opt/conda/bin/tini", "--", "/usr/share/docker/entrypoint.sh",
"/usr/share/docker/entrypoint_2.sh", "python", "-m", "notebook", "--allow-
root", "--no-browser", "--ip=*" , "--notebook-dir=/notebooks" ]  

