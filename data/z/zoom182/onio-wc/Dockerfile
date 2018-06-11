FROM alpine:edge  
  
COPY src/ /src  
  
# Set the working directory to /src  
WORKDIR /src  
  
RUN apk update  
RUN apk add --no-cache tor \  
python3  
RUN apk add --update python3-dev  
RUN apk add --no-cache libxml2-dev \  
libxslt-dev \  
gcc \  
cmake \  
g++  
RUN pip3 install --upgrade pip  
  
EXPOSE 9050  
# Install any needed packages specified in requirements.txt  
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt  

