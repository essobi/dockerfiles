ARG DOCKER_REPO=scilifelablts  
FROM $DOCKER_REPO/lts-workflows-sm-scrnaseq-ci:latest  
LABEL maintainer="Per Unneberg <per.unneberg@scilifelab.se>"  
LABEL vendor="Science for Life Laboratory"  
  
ADD . /tmp/repo  
  
RUN source activate snakemake && pip install /tmp/repo && source deactivate  
  
# Overwrite default entrypoint  
ADD entrypoint.sh /opt/docker/bin/entrypoint.sh  
  
ENTRYPOINT [ "/opt/docker/bin/entrypoint.sh" ]  
  
CMD ["lts_workflows_sm_scrnaseq"]  

