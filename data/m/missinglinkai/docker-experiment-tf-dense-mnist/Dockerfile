FROM missinglinkai/frameworks:latest  
  
ADD tensorflow_mnist_classification.py tensorflow_mnist_classification.py  
  
RUN python -m pip install missinglink-sdk -U  
  
ENV PROJECT_TOKEN=HnHgRzkuOpVNTqMK  
ENV OWNER_ID=ffff-cf7d-6501-e583-8c13a14eca0d  
ENV HOST=https://missinglink-staging.appspot.com  
ENV EPOCHS=10  
CMD python tensorflow_mnist_classification.py \  
\--owner-id $OWNER_ID \  
\--project-token $PROJECT_TOKEN \  
\--epochs $EPOCHS \  
\--host $HOST  

