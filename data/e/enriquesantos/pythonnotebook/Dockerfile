FROM jupyter/scipy-notebook  
  
RUN pip install --upgrade pip  
RUN pip install xgboost tensorflow bayesian-optimization  
  
USER root  
COPY start-ssl.sh /usr/local/bin/start-ssl.sh  
RUN chmod +x /usr/local/bin/start-ssl.sh  
  
USER $NB_USER  
CMD ["start-ssl.sh"]

