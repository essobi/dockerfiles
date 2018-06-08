#  
#  
#  
FROM python:2  
MAINTAINER Xavier Logerais <xavier@logerais.com>  
  
# Create a dedicated user  
RUN useradd -m mylar  
  
# Download pre-requisites  
#RUN pip install cheetah  
# Download latest version  
USER mylar  
WORKDIR /home/mylar  
RUN git clone https://github.com/evilhero/mylar.git ./app  
  
# Create a volume for comics  
USER mylar  
WORKDIR /home/mylar  
RUN mkdir comics  
  
# Expose the mylar home  
VOLUME /home/mylar  
  
# Expose the listening port  
EXPOSE 8090  
# Launch it  
USER mylar  
WORKDIR /home/mylar  
CMD [ "python", "app/Mylar.py" ]  

