FROM frolvlad/alpine-gcc  
RUN apk add --update alpine-sdk  
COPY . /usr/src/cube  
WORKDIR /usr/src/cube  
RUN make  
RUN make tests  
CMD ["./welcome.sh"]

