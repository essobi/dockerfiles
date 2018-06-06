# base CoMSES Dockerfile  
FROM phusion/baseimage:0.10.1  
LABEL maintainer="Allen Lee <allen.lee@asu.edu>"  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"
&& apt-get install -y python3-pip \  
&& pip3 install nltk --no-cache-dir \  
&& python3 -m nltk.downloader -d /usr/local/share/nltk_data stopwords punkt  
  
ONBUILD ENV PYTHONUNBUFFERED=1 \  
COMSES_UID=2718 \  
COMSES_USER=comses \  
LANG=C.UTF-8 \  
LC_ALL=C.UTF-8  
ONBUILD RUN useradd -m --uid $COMSES_UID $COMSES_USER  

