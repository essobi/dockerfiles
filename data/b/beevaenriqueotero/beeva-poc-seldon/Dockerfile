FROM seldonio/pyseldon:latest  
  
ENV SELDON_HOME /home/seldon  
RUN mkdir -p "$SELDON_HOME"  
WORKDIR $SELDON_HOME  
  
#RUN git clone https://github.com/fergiemcdowall/reuters-21578-json  
ADD build_model_dsstne.py $SELDON_HOME/build_model_dsstne.py  
ADD data $SELDON_HOME/data  
  
#VOLUME /seldon-data  
RUN python build_model_dsstne.py  
ADD start_recommendation_microservice.py
$SELDON_HOME/start_recommendation_microservice.py  
  
CMD [ "python","/home/seldon/start_recommendation_microservice.py","--
recommender","/home/seldon/dsstne_recommender"]  
#CMD [ "python","/home/seldon/scripts/start_recommendation_microservice.py","
--recommender","/home/seldon/dsstne_recommender"]  

