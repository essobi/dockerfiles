FROM mtangaro/docker-galaxycloud-rna-workbench-tools-1  
MAINTAINER ma.tangaro@ibiom.cnr.it  
  
ENV container docker  
  
RUN echo "localhost" > /etc/ansible/hosts  
  
RUN wget https://raw.githubusercontent.com/indigo-dc/Galaxy-flavors-
recipes/master/galaxy-rna-workbench/rna_workbench_2.yml -O /tmp/tools_2.yml  
  
RUN /usr/local/bin/install-tools GALAXY_ADMIN_API_KEY /tmp/tools_2.yml && \  
/export/_conda/bin/conda clean --tarballs --yes > /dev/null  
  
# This overwrite docker-galaxycloud CMD line  
CMD /bin/mount -t cvmfs elixir-italy.galaxy.refdata /refdata/elixir-
italy.galaxy.refdata; /usr/local/bin/galaxy-startup; /usr/bin/sleep infinity  

