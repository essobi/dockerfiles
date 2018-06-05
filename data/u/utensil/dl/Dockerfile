FROM utensil/dl:models_notop  
  
RUN mkdir /data/ || true  
ADD ./init.sh /data/init.sh  
ADD ./init_deep_learning_models.py /data/init_deep_learning_models.py  
  
RUN cd /data/ && bash init.sh  

