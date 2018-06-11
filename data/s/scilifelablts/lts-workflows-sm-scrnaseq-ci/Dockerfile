##################################################  
# lts-workflows-sm-scrnaseq-ci  
#  
# CI container for lts-workflows-sm-scrnaseq  
##################################################  
ARG DOCKER_REPO=scilifelablts  
FROM $DOCKER_REPO/lts-workflows:latest  
LABEL maintainer="Per Unneberg <per.unneberg@scilifelab.se>"  
LABEL vendor="Science for Life Laboratory"  
  
ADD lts_workflows_sm_scrnaseq/environment-27.yaml /tmp/  
ADD lts_workflows_sm_scrnaseq/environment.yaml /tmp/  
  
RUN conda env update --name py2.7 \--file /tmp/environment-27.yaml && conda
clean --all  
RUN conda env update --name snakemake --file /tmp/environment.yaml && conda
clean --all  
RUN conda install -c percyfal --name snakemake pytest-ngsfixtures websocket-
client=0.44 # Downgrade due to bug in recipe  
  
ADD entrypoint.sh /opt/docker/bin/docker-entrypoint.sh  
  
ENTRYPOINT [ "/opt/docker/bin/docker-entrypoint.sh" ]  
CMD [ "/bin/bash" ]  

