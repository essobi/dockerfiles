FROM
ubuntu:16.04@sha256:7a3b062531155aa4aee0f0e01a3f4440c86dcf972b1b73ec5d988ae438bb2651  
MAINTAINER Axel Oehmichen <axelfrancois.oehmichen11@imperial.ac.uk>  
  
WORKDIR /root  
  
ADD insert_admin_user.py /root  
  
RUN apt-get update -q && apt-get upgrade -y --no-install-recommends \  
&& apt-get install -y python-dev python-pip \  
&& pip install pymongo  
  
CMD ["python", "insert_admin_user.py", "mongodb:27017", "admin"]  

