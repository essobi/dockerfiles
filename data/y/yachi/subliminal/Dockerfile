FROM gliderlabs/alpine:3.3  
RUN apk add --update --no-cache ca-certificates python py-pip  
  
RUN pip install --upgrade pip  
RUN pip install subliminal==1.1.1  
  
RUN mkdir ~/.config  
  
RUN mkdir /subs  
  
WORKDIR /subs  
  
VOLUME ["/subs"]  
  
ENTRYPOINT ["subliminal"]  

