FROM aghorbani/mapd-pygdf  
MAINTAINER Asghar Ghorbani [https://de.linkedin.com/in/aghorbani]  
  
# Configure environment  
ARG XGBOOST_COMMIT="332b26d"  
# Add xgboost  
RUN git clone \--recursive https://github.com/dmlc/xgboost.git && cd xgboost
&& git checkout $XGBOOST_COMMIT && \  
make PLUGIN_UPDATER_GPU=ON && \  
cd python-package && \  
/bin/bash -c "source activate pycudf_notebook_py35 && python setup.py install"
&& \  
cd ~ && rm -rf xgboost  
  
# Add scikit-learn  
RUN /bin/bash -c "source activate pycudf_notebook_py35 && \  
conda install -y scikit-learn && \  
conda clean -iltpsy "  
  
# Add jaydebeapi  
RUN /bin/bash -c "source activate pycudf_notebook_py35 && pip install
jaydebeapi"  
  
# Add some samples  
RUN cd ~/notebooks/ && git clone
https://github.com/a-ghorbani/goai_samples.git  
  
EXPOSE 9090 9091 9092 9093  
EXPOSE 8888  
ENTRYPOINT ["./scripts/start.sh"]  
CMD ["--jupyter-args='--ip=*'"]  
  

