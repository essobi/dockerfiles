FROM flyinprogrammer/mesos-base  
MAINTAINER Alan Scherger <flyinprogrammer@gmail.com>  
  
RUN apt-get install -y marathon && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
  
COPY app.json /app.json  
ENV CONTAINERPILOT=file:///app.json  
EXPOSE 8080  
CMD ["/bin/containerpilot", "/usr/bin/marathon"]  

