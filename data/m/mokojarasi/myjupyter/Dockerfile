From alpine:3.7  
Maintainer Yamanaka Hirofumi  
  
Run apk add --no-cache python3 git zeromq \  
python3-dev gcc linux-headers zeromq-dev musl-dev && \  
pip3 install jupyter nbconvert && \  
apk del --purge python3-dev gcc linux-headers zeromq-dev musl-dev  
  
Expose 8888  
Cmd jupyter notebook --ip=0.0.0.0 --allow-root  
  

