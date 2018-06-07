FROM node:8.1  
# Install yarn  
RUN curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version 0.26.1  
  
# Copy source code  
COPY . /app  
  
# Change working directory  
WORKDIR /app  
  
# Install dependencies  
RUN /usr/local/bin/yarn  
  
# Expose API port to the outside  
EXPOSE 8000  
# Launch application  
CMD /usr/local/bin/yarn prod:build && /usr/local/bin/yarn prod:start  

