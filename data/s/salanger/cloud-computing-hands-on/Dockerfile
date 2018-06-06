FROM alpine:3.5  
RUN apk add --update py2-pip  
RUN pip install --no-cache-dir web.py  
RUN pip install --no-cache-dir delegator.py  
COPY pdfmagic.py /usr/src/app/  
COPY favicon.ico /usr/src/app/  
EXPOSE 8080  
CMD ["python", "/usr/src/app/pdfmagic.py"]  

