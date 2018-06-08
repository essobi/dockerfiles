FROM godatadriven/pyspark  
  
ARG BUILD_DATE  
  
LABEL org.label-schema.name="JupyterHub + PySpark $SPARK_VERSION" \  
org.label-schema.build-date=$BUILD_DATE  
RUN conda install -y nb_conda jupyterhub jupyter_client -c conda-forge && \  
python -m nb_conda_kernels.install --enable \--prefix=/opt/miniconda3 && \  
conda clean -tipsy && \  
apt-get update && \  
apt-get install -y openjdk-8-jre git build-essential nano vim less procps
--no-install-recommends && \  
apt-get clean  
  
EXPOSE 8000  
ENTRYPOINT ["jupyterhub"]

