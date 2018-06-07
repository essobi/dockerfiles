FROM ros:latest  
LABEL maintainer="bat-cha <baptiste.chatrain@gmail.com>"  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
python3-pip \  
python3-setuptools \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /app  
VOLUME "/app"  
WORKDIR "/app"  
EXPOSE 11311  
COPY requirements.txt /app/requirements.txt  
  
RUN pip3 install --upgrade pip  
RUN pip3 install
http://download.pytorch.org/whl/cpu/torch-0.3.1-cp35-cp35m-linux_x86_64.whl  
RUN pip3 install -r /app/requirements.txt  
  

