FROM frolvlad/alpine-python2  
EXPOSE 80  
#install dependencies  
RUN apk add --update bash  
  
COPY countdown.sh /  
  
#RUN the countdown on stdout  
CMD bash /countdown.sh  
  
#TODO: run the countdown on the webserver  
#RUN touch index.html  
#CMD python index.py  

