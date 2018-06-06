# EEG-Classifier  
FROM python:slim  
MAINTAINER Flywheel <support@flywheel.io>  
  
# Flywheel spec (v0)  
WORKDIR /flywheel/v0  
  
# Copy executables into place  
COPY eeg_classifier.py ./run  
COPY manifest.json .  
RUN chmod +x run manifest.json  
  
# Set the entrypoint  
ENTRYPOINT ["/flywheel/v0/run"]  

