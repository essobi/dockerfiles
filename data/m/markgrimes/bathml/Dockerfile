FROM tensorflow/tensorflow  
  
RUN pip install keras  
  
# Need to install git because it's not in the base image  
RUN apt-get update \  
&& apt-get install -y git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN cd /notebooks \  
&& git clone https://github.com/owenjonesuob/keras-workshop  
  

