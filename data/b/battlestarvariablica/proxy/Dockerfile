FROM docker  
  
ENV USER=root  
ENV HOME=/root  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin  
  
RUN mkdir /app  
WORKDIR /app  
  
EXPOSE 2323  
RUN apk add --update python3  
  
RUN python3 --version  
  
CMD ["python3", "-u", "proxy.py", "2323"]  
  
ADD proxy.py /app  

