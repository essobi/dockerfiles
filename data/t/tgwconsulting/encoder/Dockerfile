FROM python:3  
WORKDIR /usr/src/audio_encoder  
  
ADD . /usr/src/audio_encoder  
RUN mkdir /var/input  
RUN mkdir /var/output  
RUN chmod 766 /var/input  
RUN chmod 766 /var/output  
  
#COPY requirements.txt ./  
#RUN pip install --no-cache-dir -r requirements.txt  
# Define environment variable  
ENV INPUT_FOLDER=/var/input  
ENV OUTPUT_FOLDER=/var/output  
ENV BLOB_NAME=some_blob  
  
# Run FileSentry.py when the container launches  
CMD ["python", "FileSentry.py"]  

