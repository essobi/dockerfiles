FROM continuumio/miniconda3:4.4.10  
  
ENV PATH="/opt/conda/bin:${PATH}"  
# https://github.com/ContinuumIO/docker-images/issues/79  
RUN conda update conda -y  
  
RUN conda install python=3.6 -y  
  
RUN conda config \--add channels conda-forge  
  
RUN conda install jupyter jupyterlab matplotlib seaborn pandas numpy scipy
scikit-learn statsmodels nltk textblob xgboost tensorflow keras -y  
  
VOLUME ["/notebooks"]  
EXPOSE 8888  
  
COPY ./docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

