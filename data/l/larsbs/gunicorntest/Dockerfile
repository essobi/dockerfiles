# Docker image for eTeach  
FROM ubuntu:14.04  
# Environment configuration  
ENV DJ_VERSION 1.7.7  
# Install pip  
RUN apt-get update && apt-get install -y \  
python3-pip  
  
# Install python packages  
RUN pip3 install --upgrade pip  
RUN pip3 install \  
django==$DJ_VERSION \  
dj-static \  
dj-database-url \  
gunicorn \  
honcho  
  
# Add project  
COPY gunicorntest /data/gunicorntest  
  
# Define working directory  
WORKDIR /data/gunicorntest  
  
# Define default command  
CMD ["honcho", "start"]  
  
# Expose ports  
EXPOSE 8000  

