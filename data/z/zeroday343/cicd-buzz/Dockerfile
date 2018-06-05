FROM alpine:3.5  
RUN apk add --update python py-pip  
COPY requirements /src/requirements  
RUN pip install -r /src/requirements  
COPY app.py /src  
COPY buzz /src/buzz  
COPY static /src/static  
COPY templates /src/templates  
CMD python /src/app.py  

