FROM python:3.6-onbuild  
VOLUME /config  
RUN apt-get update && apt-get install -y \  
build-essential \  
checkinstall \  
libreadline-gplv2-dev \  
libncursesw5-dev \  
libssl-dev \  
libsqlite3-dev \  
tk-dev \  
libgdbm-dev \  
libc6-dev \  
libbz2-dev \  
libudev-dev \  
libxslt-dev \  
libxml2-dev \  
net-tools \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --upgrade pip  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Reuse home-assistant script to build python openzwave.  
RUN wget https://raw.githubusercontent.com/home-assistant/home-
assistant/dev/virtualization/Docker/scripts/python_openzwave  
RUN chmod +x python_openzwave  
RUN ./python_openzwave  
  
ADD . /usr/src/app/firefly  
WORKDIR /usr/src/app/firefly  
  
CMD ["python3", "./main.py"]  
  
EXPOSE 6002  

