FROM p3lim/alpine:3.7  
# install dependencies  
RUN apk add --no-cache python3 sqlite  
  
# install paste and its dependencies  
RUN apk add --no-cache -t build-deps git  
RUN git clone https://github.com/p3lim/paste /tmp/paste  
RUN pip3 install -r /tmp/paste/requirements.txt  
RUN cp -r /tmp/paste/src/* /app  
  
# cleanup  
RUN apk del build-deps  
RUN rm -rf /tmp/*  
  
# copy local files  
COPY root/ /  
  
# expose ourselves  
EXPOSE 8080  
VOLUME /config  

