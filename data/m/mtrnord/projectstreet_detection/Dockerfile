FROM mtrnord/opencv:latest  
  
MAINTAINER MTRNord <info@nordgedanken.de>  
  
RUN apt-get install -y cron git python-pip python-dev  
RUN git clone https://github.com/facebook/zstd.git && cd zstd && git checkout
master && make && make install  
COPY scripts/ PStreet  
ENV TF_BINARY_URL
https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc0-cp27-none-
linux_x86_64.whl  
RUN pip install --upgrade $TF_BINARY_URL  
WORKDIR PStreet  
CMD cron  

