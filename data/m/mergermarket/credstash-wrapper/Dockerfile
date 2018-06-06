FROM alpine:3.5  
RUN apk --no-cache add python python-dev py-pip build-base openssl-dev libffi-
dev  
RUN pip install --upgrade pip  
RUN pip install credstash  
RUN mkdir /credstash  
WORKDIR /credstash  
COPY ./credstash.sh .  
  
ENTRYPOINT [ "/credstash/credstash.sh" ]

