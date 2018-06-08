FROM ubuntu:latest  
MAINTAINER = Aman Mangal <amanmangal@gatech.edu>  
  
# install tools and dependencies  
RUN apt-get update && apt-get install -y \  
git \  
python \  
python-dev \  
python-pip  
  
# install python dependencies  
RUN pip install bitarray \  
ipaddr \  
netaddr \  
networkx \  
yappi  
  
# install pox  
RUN git clone http://github.com/noxrepo/pox  
  
# install pyretic  
RUN git clone http://github.com/mangalaman93/pyretic.git  
  
# setting up path  
ENV PATH /pox/:/pyretic/:$PATH  
ENV PYTHONPATH /pox/:/pyretic/:$PYTHONPATH  
  
# expose ports  
EXPOSE 6633  
# copy policies  
COPY policy.py /pyretic/pyretic/examples/  
  
# command to run  
ENTRYPOINT ["pyretic.py"]  

