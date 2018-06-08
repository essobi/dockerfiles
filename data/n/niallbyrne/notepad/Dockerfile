FROM frolvlad/alpine-python3  
MAINTAINER Niall Byrne <reading.crows@gmail.com>  
  
# Create the RUN AS user  
RUN adduser -h /home/webservice -s /bin/ash webservice -D  
USER webservice  
WORKDIR /home/webservice  
  
# Configure the Home Directory  
ADD requirements /home/webservice/requirements  
ADD notepad /home/webservice/notepad  
ADD bin /home/webservice/bin  
  
# Install the application  
USER root  
RUN chown -R webservice:webservice /home/webservice  
RUN bin/build.sh  
  
# Configure Container Ports  
EXPOSE 8000  
  
# Start the application  
CMD bin/launch.sh  

