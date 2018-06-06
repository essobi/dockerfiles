# Dockerfile written by James Bielman <jamesjb@tozny.com>  
#  
# Copyright (C) 2016, Tozny, LLC.  
FROM alpine:3.4  
RUN apk --no-cache add libc-dev gcc make python-dev py-pip  
RUN pip install credstash  
ENV AWS_REGION=us-west-2  
CMD ["credstash"]  

