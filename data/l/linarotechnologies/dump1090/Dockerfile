# derive from our baseimage  
FROM linarotechnologies/rtl-sdr:latest  
  
WORKDIR /tmp  
  
RUN apk add --no-cache alpine-sdk git  
  
RUN git clone git://github.com/mutability/dump1090.git && \  
cd dump1090 && \  
make  
  
WORKDIR /tmp/dump1090  
  
ENTRYPOINT ["./dump1090", "--interactive","--net","--metric"]  

