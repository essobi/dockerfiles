FROM python:rc-slim  
  
MAINTAINER Javier Fernández-Bravo Peñuela - fraferp9@posgrado.upv.es  
  
RUN apt-get update  
RUN apt-get install --no-install-recommends --assume-yes imagemagick  
RUN apt-get clean  
  
ADD requirements.txt /  
RUN pip3 install -r requirements.txt  
  
ADD image_processor_lambda.py /  
  
# Required to avoid relying on symlinks, which fails when using udocker and
the F1 execution mode on AWS Lambda  
ENV PATH /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/:$PATH  
  

