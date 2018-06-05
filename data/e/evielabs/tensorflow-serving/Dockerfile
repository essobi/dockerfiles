FROM ubuntu  
  
ADD https://s3-us-west-2.amazonaws.com/cloudvm-public/tensorflow_model_server
/usr/bin/tensorflow_model_server  
RUN chmod +x /usr/bin/tensorflow_model_server  
  
EXPOSE 31501  
WORKDIR /model-data  
  
#CMD ["tensorflow_model_server", "--model_base_path=/model-data", "--
port=31501", "--enable_batching=true"]  
CMD ["tensorflow_model_server", "--model_base_path=/model-data", "--
port=31501"]  

