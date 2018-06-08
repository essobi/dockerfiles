FROM python:alpine  
MAINTAINER Haluk <haluk.tutuk@periscube.com>  
  
# no need to keep cache, reduce the size  
RUN pip --no-cache-dir install flask  
  
WORKDIR /app  
COPY hello-world.py .  
  
# web app port  
EXPOSE 8080  
ENTRYPOINT ["python"]  
CMD ["hello-world.py"]

