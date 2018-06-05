FROM python:3.6-slim  
  
MAINTAINER Gabriele Giammatteo <gabriele.giammatteo@eng.it>  
  
  
RUN apt-get update  
RUN apt-get -y install git  
  
# since the pip install commands would be cached, add this line that generates
a random content to add to the container and  
# invalidates all the steps that follows  
ADD
https://www.random.org/strings/?num=16&len=16&digits=on&upperalpha=on&loweralpha=on&unique=on&format=plain&rnd=new
uuid  
  
RUN pip install git+https://github.com/benchmarking-suite/benchsuite-
scheduler.git#egg=benchsuite.scheduler  
  
ENTRYPOINT ["benchsuite-scheduler", "--config", "/tmp/config"]  

