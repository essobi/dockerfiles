# VERSION 1.1  
FROM phusion/baseimage:0.10.1  
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
build-essential \  
unzip \  
wget \  
gnuplot  
  
ENV VERSION fc71268  
ENV FOLDER_NAME pmbw  
  
WORKDIR /root  
RUN wget https://codeload.github.com/bingmann/pmbw/zip/"${VERSION}" && \  
unzip -qo "${VERSION}" && \  
rm "${VERSION}" && \  
mv pmbw-"${VERSION}" "$FOLDER_NAME"  
  
WORKDIR /root/$FOLDER_NAME  
RUN ./configure && make  
  
# Clean Up  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root  
COPY run.sh .  
ENTRYPOINT ["/sbin/my_init", "--skip-startup-files", "--quiet", "--",
"./run.sh"]  

