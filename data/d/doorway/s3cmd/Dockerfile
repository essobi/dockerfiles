FROM ubuntu:14.04  
# Update Ubuntu and install common packages  
RUN apt-get update -y && apt-get install -y wget && apt-get install -y python-
setuptools  
  
RUN wget
https://github.com/s3tools/s3cmd/releases/download/v1.5.2/s3cmd-1.5.2.tar.gz
&& \  
tar xzvf s3cmd-1.5.2.tar.gz && \  
cd s3cmd-1.5.2 && \  
python setup.py install && \  
cd / && \  
rm -rf s3cmd-1.5.2*  
  
ADD files/s3cfg /.s3cfg  
ADD files/main.sh /main.sh  
  
# Main entrypoint script  
RUN chmod 777 main.sh  
  
WORKDIR /tmp  
  
ENTRYPOINT [ "/main.sh" ]  

