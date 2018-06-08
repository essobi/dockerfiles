FROM python:3.5  
MAINTAINER Olivier Tabone <olivier.tabone@ripplemotion.fr>  
EXPOSE 5000  
RUN ["mkdir", "-p", "/tmp/build"]  
COPY . /tmp/build  
RUN ["pip", "install", "/tmp/build"]  
RUN ["rm", "-rf", "/tmp/build"]  
CMD ["whats-my-ip-server"]  

