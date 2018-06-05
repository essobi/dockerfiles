FROM ubuntu:16.04  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/alessmar/Dockerfiles.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0.0-rc1"  
  
RUN apt-get update -y && apt-get install -y apt-utils \  
context \  
curl\  
gcc \  
libssl-dev \  
make \  
pandoc \  
python \  
python-dev \  
python-tk  
  
RUN curl -OL https://bootstrap.pypa.io/get-pip.py && python get-pip.py  
RUN pip install --upgrade matplotlib \  
numpy \  
watson-developer-cloud  
  
ENV BASE_PATH=/resume/  
  
RUN mkdir $BASE_PATH  
WORKDIR $BASE_PATH  
  
RUN curl -OL
https://raw.githubusercontent.com/mszep/pandoc_resume/master/style_chmduquesne.css
&& \  
curl -OL
https://raw.githubusercontent.com/mszep/pandoc_resume/master/style_chmduquesne.tex  
  
ADD Makefile tone.py $BASE_PATH  
  
ENTRYPOINT ["make"]  

