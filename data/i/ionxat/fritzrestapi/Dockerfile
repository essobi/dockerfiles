# docker rmi fritzrestapi  
# docker build -t fritzrestapi .  
# docker run --name fritzrestapi -p 3000:3000 -d fritzrestapi  
# Use the official debian runtime as a parent image  
FROM debian:stretch-slim  
  
# Install the basic things  
RUN apt-get update \  
&& apt-get install -y \  
sudo \  
curl \  
gnupg1 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get install -y nodejs  
  
# Copy nodejs service  
COPY . /opt/  
  
# Set the working directory  
WORKDIR /opt/  
  
# Run service  
RUN npm install  
  
# Run node at startup  
CMD node ./bin/www  
  
# Expose port 8000  
EXPOSE 3000

