FROM mayoqin/gruntubuntu  
LABEL maintainer "Panagiotis Korfiatis korfiatis.panagiotis@mayo.edu"  
  
WORKDIR /  
  
# Build information  
ARG BUILD_DATE  
ARG GIT_REF  
  
LABEL org.label-schema.build-data=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/radiomics/pyradiomics.git" \  
org.label-schema.vcs-ref=$GIT_REF \  
org.label-schema.schema-version="1.0.0-rc1"  
  
RUN apt-get -y update && apt-get install -y \  
wget \  
curl\  
unzip \  
build-essential \  
xutils-dev \  
default-jre \  
python3-pip \  
cmake  
  
RUN mkdir -p /grunt  
WORKDIR /  
RUN wget -O dcmqi-linux.tar.gz --quiet
https://github.com/QIICR/dcmqi/releases/download/latest/dcmqi-1.0.5-linux-20171124-3f6534e.tar.gz  
RUN mkdir -p /grunt/dcmqi-linux  
RUN tar -xvzf dcmqi-linux.tar.gz -C /grunt/dcmqi-linux --strip-components 1  
COPY dcmqi.gruntfile.yml /grunt.d/gruntfile.yml  
# Configure Slicer environment  
ENV PATH=/grunt/dcmqi-linux/bin:${PATH}  
# What do we run on startup?  
CMD ["/bin/grunt", "/grunt.d/gruntfile.yml"]  
# We expose port 9901 by default  
EXPOSE 9901:9901  

