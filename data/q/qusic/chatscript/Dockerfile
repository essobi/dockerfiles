FROM alpine:latest  
  
RUN apk --no-cache upgrade \  
&& apk --no-cache add libgcc libstdc++ libcurl \  
&& apk --no-cache add --virtual .build-deps build-base curl-dev  
WORKDIR /bot  
COPY SRC SRC  
COPY privatecode privatecode  
RUN mkdir BINARIES \  
&& DEFINES="-I../privatecode/cppjieba/include -I../privatecode/cppjieba/deps
-DPRIVATE_CODE" make -C SRC clean server \  
&& rm -rf privatecode \  
&& apk del .build-deps  
  
COPY DICT DICT  
COPY LIVEDATA LIVEDATA  
COPY privatecode/cppjieba/dict JIEBADATA  
COPY RAWDATA/files0.txt RAWDATA/  
COPY RAWDATA/ONTOLOGY RAWDATA/ONTOLOGY  
COPY RAWDATA/WORLDDATA RAWDATA/WORLDDATA  
RUN mkdir TOPIC VERIFY /data \  
&& cd BINARIES \  
&& ./ChatScript users=/data logs=/data tmp=/data local build0=files0.txt \  
&& rm -rf /data  
  
ONBUILD COPY *.top ../RAWDATA/BOT/  
ONBUILD RUN echo RAWDATA/BOT/ > ../RAWDATA/filesbot.txt \  
&& ./ChatScript users=/data logs=/data tmp=/data local build1=filesbot.txt \  
&& rm -rf /data  
  
WORKDIR /bot/BINARIES  
ENTRYPOINT ["./ChatScript", "users=/data", "logs=/data", "tmp=/data"]  
EXPOSE 1024  

