FROM python  
MAINTAINER NOSPAM <nospam@nnn.nnn>  
  
COPY page-check.py /page-check.py  
RUN chmod +x /page-check.py  
  
ENV PYTHONUNBUFFERED=0  
CMD ["sh", "-c", "PYTHONUNBUFFERED=0 eval /page-check.py $OPTIONS"]  

