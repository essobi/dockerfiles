FROM python:3.5.5  
# Define environment variable  
ENV SOURCE_IMAGE default_source_image  
ENV DESTINATION_IMAGE default_destination_image  
ENV SIZE default_size  
ENV DESTINATION_COLLECTION default_size  
  
WORKDIR /  
  
ADD make_thumbnail.py /  
  
RUN apt-get install -y libjpeg-dev && pip install pillow  
  
# Run app.py when the container launches  
CMD ["sh", "-c", "python ./make_thumbnail.py ${SIZE}x${SIZE}
/src/${SOURCE_IMAGE} /dst/${DESTINATION_IMAGE} ${DESTINATION_COLLECTION}"]  

