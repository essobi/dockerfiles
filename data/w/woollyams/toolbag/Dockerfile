FROM
alpine:3.7@sha256:7df6db5aa61ae9480f52f0b3a06a140ab98d427f86d8d5de0bedab9b8df6b1c0  
  
MAINTAINER https://github.com/mdub/toolbox-image  
  
RUN apk --no-cache add \  
bash \  
bind-tools \  
curl \  
diffutils \  
httpie \  
py-pip \  
python  
  
RUN pip install httpie-oauth  
  
CMD ["bash"]  

