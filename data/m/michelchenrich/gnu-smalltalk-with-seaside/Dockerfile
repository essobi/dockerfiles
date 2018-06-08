FROM ubuntu:latest  
  
RUN apt-get update  
RUN apt-get install -y git gnu-smalltalk  
  
WORKDIR /app  
  
RUN gst-package --download Grease  
RUN gst-package --download Iliad  
  
COPY . /app  
RUN gst build_image.st  
  
CMD ["gst-remote", "-I", "prod.im", "--server"]  
  
EXPOSE 8080  

