FROM ubuntu:latest  
MAINTAINER David Robbins <robbins.david@gmail.com>  
  
RUN apt-get update && apt-get install -y curl  
RUN curl https://install.meteor.com/ | sh  
  
COPY entrypoint.sh /usr/bin/entrypoint.sh  
RUN chmod +x /usr/bin/entrypoint.sh  
  
EXPOSE 3000  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
CMD []  
  
ONBUILD COPY . /opt/src  
ONBUILD WORKDIR /opt/src  
ONBUILD RUN mkdir -p /opt/app && meteor build --directory /opt/app  

