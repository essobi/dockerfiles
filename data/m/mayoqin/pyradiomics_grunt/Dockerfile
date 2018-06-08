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
unzip \  
build-essential \  
xutils-dev \  
default-jre \  
python3-pip \  
cmake  
  
RUN pip3 install wget  
RUN pip3 install requests  
RUN git clone https://github.com/Radiomics/pyradiomics.git  
RUN cd pyradiomics && pip3 install -r requirements.txt && python3 setup.py
install  
  
WORKDIR /  
  
COPY pyradiomic.grunt.yml /grunt.d/gruntfile.yml  
  
CMD ["/bin/grunt", "/grunt.d/gruntfile.yml"]  
# We expose port 9901 by default  
EXPOSE 9901:9901  

