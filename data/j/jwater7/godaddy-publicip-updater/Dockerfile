FROM python  
LABEL maintainer "j"  
  
RUN pip install requests  
RUN pip install pif  
RUN pip install -I godaddypy==2.2.6  
  
COPY godaddy-publicip-updater.py /  
  
CMD [ "python", "-u", "/godaddy-publicip-updater.py" ]  
  

