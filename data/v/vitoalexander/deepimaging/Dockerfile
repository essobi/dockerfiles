FROM tensorflow/tensorflow:0.12.0-rc1-devel  
  
# Download models repository  
WORKDIR /home  
RUN git clone https://github.com/tensorflow/models.git  
  
# Check out comaptible version  
WORKDIR /home/models  
RUN git checkout 12f279d6f4cb33574bc20109b41eb8a59f40cfd1  
  
# Apply patch  
COPY patches/im2txt.patch im2txt.patch  
RUN git apply im2txt.patch  
  
# Build im2txt  
WORKDIR /home/models/im2txt  
RUN bazel build --ignore_unsupported_sandboxing -c opt im2txt/run_inference  
  
# Install dependencies  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs imagemagick wget  
RUN npm install apidoc -g  
  
# Copy sources and install dependencies  
WORKDIR /home/server  
COPY package.json package.json  
RUN npm install  
COPY index.js index.js  
COPY src src  
COPY apidoc.json apidoc.json  
COPY bin-docker bin  
RUN chmod +x bin/*.sh  
COPY public public  
RUN apidoc -i src/ -o apidoc  
  
# Create directory for upload  
RUN mkdir tmp  
  
# Entry point  
ENTRYPOINT ["nodejs", "index.js"]  

