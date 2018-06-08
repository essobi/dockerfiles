# Set the base image to Ubuntu  
FROM python:3-onbuild  
CMD [ "python", "/home/lena.py" ]  
  
# File Author / Maintainer  
MAINTAINER Paulina Lach  
  
RUN apt-get update  
RUN apt-get install -y build-essential gfortran libblas-dev libatlas-dev
liblapack-dev  
  
RUN pip install scipy  
  
ADD ./lena.py /home/lena.py  
RUN chmod 777 /home/lena.py  
  
ENTRYPOINT /home/lena.py  

