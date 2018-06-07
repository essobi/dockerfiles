FROM fermipy/fermipy:latest  
MAINTAINER Stephan Zimmer <zimmer@slac.stanford.edu>  
RUN cd /home  
RUN mkdir /home/pointlike  
RUN mkdir /home/apps  
ADD apps/gtlike2gtobssimConverter.py /home/apps/gtlike2gtobssimConverter.py  
ADD apps/makeSkyModelFromCatalog.py /home/apps/makeSkyModelFromCatalog.py  
RUN chmod u+x /home/apps/*.py  
RUN echo 'export PATH=/home/apps:${PATH}' >> /root/.bashrc  
RUN curl -o pointlike.tgz -k -L
https://dampevm3.unige.ch/misc/pointlike-20170824.tgz && \  
tar xzvf pointlike.tgz -C /home && \  
echo 'export PYTHONPATH=/home/pointlike/python:${PYTHONPATH}' >> /root/.bashrc  
RUN ls -la /home  
CMD ["usleep 10 && /opt/conda/bin/jupyter notebook --notebook-dir=/workdir
--ip='*' --port=8888 --no-browser --allow-root"]  
ENTRYPOINT ["/bin/bash","--login","-c"]

