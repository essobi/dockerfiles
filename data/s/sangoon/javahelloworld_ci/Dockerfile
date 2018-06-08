FROM debian  
#Modified by sangoon  
#RUN apt-get update -qq && apt-get install -qy vim wget  
#ENTRYPOINT ["ping", "-c", "30"]  
#CMD ["127.0.0.1"]  
RUN mkdir /data/myvol -p  
RUN echo "Lucy in the Sky with Docker" > /data/myvol/test  
VOLUME /data/myvol  
EXPOSE 80 8080  

