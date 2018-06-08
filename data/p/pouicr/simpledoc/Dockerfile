FROM debian:jessie  
  
MAINTAINER loic.rodier@gmail.com  
  
RUN apt-get update --fix-missing\  
&& apt-get install -y python-pip python-dev build-essential linkchecker \  
&& pip install mkdocs \  
&& apt-get clean  
  
ADD theme /theme  
ADD export.sh /  
RUN chmod +x /export.sh  
#RUN useradd doc  
RUN mkdir /work  
#RUN chown doc:doc /work  
WORKDIR /work  
  
#USER doc  
ENTRYPOINT ["mkdocs"]  
CMD ["serve"]  

