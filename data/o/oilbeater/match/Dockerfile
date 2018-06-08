FROM python:2  
RUN pip install tornado  
RUN pip install requests  
EXPOSE 80  
COPY . /myweb/  
WORKDIR /myweb/  
CMD python getimage.py  

