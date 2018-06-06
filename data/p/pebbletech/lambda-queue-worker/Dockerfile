FROM node:6-slim  
  
# Install git  
RUN apt-get update \  
&& apt-get install -qy git python build-essential \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install node modules  
RUN npm install -g git+https://git@github.com/deviavir/sqs-to-
lambda.git#function-name-environment  
  
# Setup user  
RUN useradd -g daemon -m -d /app app  
RUN chown -R app /app  
USER app  
WORKDIR /app  
ENV HOME /app  
  
# Default command to run on boot  
CMD sqs-to-lambda  

