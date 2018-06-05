FROM timbr/juno-machine-kernel:development  
  
USER gremlin  
WORKDIR /home/gremlin  
RUN /anaconda/envs/juno/bin/conda install -n juno -y scikit-image pandas
seaborn scipy  
RUN /anaconda/envs/juno/bin/conda install -n juno -y -c menpo ffmpeg=3.1.3  
RUN /anaconda/envs/juno/bin/pip install mercantile runipy  
RUN /anaconda/envs/juno/bin/conda install -n juno -y -c conda-forge
rasterio>=1.0a5 descartes  
  
RUN /anaconda/envs/juno/bin/conda install -n juno -y -c
https://conda.anaconda.org/t/ch-04d4a9f2-9c39-4ea9-bd7a-6945296c768f/timbr-io
protogen  
  
USER root  
RUN chmod g-rw /anaconda/envs/juno/bin/protogen  
RUN chmod u-rw /anaconda/envs/juno/bin/protogen  
RUN mkdir /task  
RUN chown -R gremlin /task  
RUN chmod -R go+w /task  
ADD task_runner.py /task/task_runner.py  
  
WORKDIR /gbdxtools  
RUN git clone -b radd-dev https://github.com/DigitalGlobe/gbdxtools /gbdxtools  
RUN /anaconda/envs/juno/bin/pip install .  
  
RUN /anaconda/bin/conda install -n juno -y curl=7.52.1 pycurl  
  
RUN /anaconda/envs/juno/bin/pip uninstall -y gbdx-auth  
USER root  
WORKDIR /gbdx-auth  
#RUN git clone -b env-vars-existing-tokens https://github.com/saintsjd/gbdx-
auth /gbdx-auth  
RUN git clone -b gbdx-runtime-support https://github.com/saintsjd/gbdx-auth
/gbdx-auth  
RUN /anaconda/envs/juno/bin/pip install -r requirements.txt  
RUN /anaconda/envs/juno/bin/pip install .  
  
RUN chown -R gremlin /gbdxtools  
RUN chown -R gremlin /gbdx-auth  
  
USER gremlin  
WORKDIR /home/gremlin  
  

