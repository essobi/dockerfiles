FROM alpine:3.4  
WORKDIR /app  
COPY builder/gikou .  
RUN wget http://s3-ap-
northeast-1.amazonaws.com/naoys.gikou.binary/binary_20160606.zip && \  
unzip binary_20160606.zip && \  
rm binary_20160606.zip && \  
mv binary/* . && \  
rm -rf binary  
CMD ["./gikou"]  

