FROM alpine:latest  
RUN apk add --update py-pip ca-certificates && pip install lemonsync  
WORKDIR /working_dir  
VOLUME ['/working_dir']  
CMD ["lemonsync", "-c", "/working_dir/lemonsync.cfg"]

