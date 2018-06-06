FROM ubuntu:latest  
  
# Update OS  
#RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install Python  
RUN apt-get install -y python-dev python-pip  
  
# Add requirements.txt  
RUN mkdir /opt/chatterbot  
ADD requirements.txt /opt/requirements.txt  
  
# Install uwsgi Python web server  
RUN pip install uwsgi  
# Install app requirements  
RUN pip install -r /opt/requirements.txt  
  
# Create app directory  
ADD . /opt/chatterbot  
  
# Set the default directory for our environment  
ENV HOME /opt/chatterbot  
WORKDIR /opt/chatterbot  
  
# Expose port 8000 for uwsgi  
EXPOSE 9019  
ENTRYPOINT ["uwsgi"]  
CMD ["--http", "0.0.0.0:9019", "--module", "app:app", "--processes", "1", "--
threads", "8"]  

