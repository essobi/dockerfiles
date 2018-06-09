FROM flyinprogrammer/mesos-base  
MAINTAINER Alan Scherger <flyinprogrammer@gmail.com>  
  
COPY app.json /app.json  
ENV CONTAINERPILOT=file:///app.json  
EXPOSE 5050  
CMD ["/bin/containerpilot", "mesos-master"]

