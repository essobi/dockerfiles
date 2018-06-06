FROM busybox:latest  
  
RUN mkdir -p /dataset  
WORKDIR /dataset  
  
ENV URL=http://www.openslr.org/resources/12/train-clean-100.tar.gz  
ENV NAME=train-clean-100  
ENV MD5=2a93770f6d5c6c964bc36631d331a522  
  
RUN wget -O ./data.tar.gz "$URL" \  
&& echo "$MD5 data.tar.gz" > md5sum \  
&& md5sum -c md5sum \  
&& rm md5sum \  
&& gzip -d ./data.tar.gz \  
&& mkdir $NAME \  
&& tar -x -f ./data.tar -C $NAME \  
&& rm -rf ./data.tar  
  
VOLUME /dataset/$NAME  
  

