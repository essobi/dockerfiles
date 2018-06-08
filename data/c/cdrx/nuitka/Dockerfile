FROM ubuntu:16.04  
RUN apt update && apt upgrade -y && apt install -y build-essential python3-pip
chrpath python libmysqlclient-dev libjpeg-dev zlib1g-dev && rm -rf
/var/lib/apt/lists/*  
RUN pip3 install nuitka==0.5.28  
WORKDIR /src  
CMD nuitka  

