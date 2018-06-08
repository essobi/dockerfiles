FROM docker.io/weischenfeldt/computerome_weischenfeldt_docker:latest  
MAINTAINER Francesco Favero <francesco.favero@bric.ku.dk>  
  
USER root  
  
ADD pype_modules/repos.yaml /root/repos.yaml  
  
RUN pip install --no-cache-dir bio_pype \  
&& pype repos --repo /root/repos.yaml install weischenfeldt_stable \  
&& pype repos --repo /root/repos.yaml install --force weischenfeldt_docker \  
&& rm /root/repos.yaml \  
&& mkdir /databases && chmod -R 7777 /databases \  
&& mkdir /data && chmod -R 7777 /data  
  
VOLUME /databases /data  
ADD scripts/* /usr/bin/  
ADD scripts/run_delly_pipeline.py /usr/bin/run_delly_pipeline  
RUN chmod +x /usr/bin/run_delly_pipeline  
RUN chmod +x /usr/bin/delly.Rmd  
RUN chmod +x /usr/bin/proc_time.py  
  
USER docker  
  
WORKDIR /home/docker  
  
CMD ["/bin/bash"]  

