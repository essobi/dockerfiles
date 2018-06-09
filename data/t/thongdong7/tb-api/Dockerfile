FROM python:2.7  
ADD entry.sh /  
WORKDIR /code  
  
RUN cd /code \  
&& virtualenv venv  
  
EXPOSE 80  
ENV SLEEP 5  
ENV EXTRAS_REQUIRE ""  
ENV ENV local  
  
VOLUME /code  
  
ENTRYPOINT ["bash", "/entry.sh"]  

