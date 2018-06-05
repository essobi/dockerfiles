FROM amazonlinux:2017.12  
RUN yum update -y && \  
yum install gcc zlib zlib-devel openssl openssl-devel libffi libffi-devel wget
zip -y && \  
yum clean all  
  
# Install python3.6.2, using the method described in amazonlinux image
documentation's  
# "How do I install a software package from Extras repository in Amazon Linux
2 LTS Candidate?"  
RUN amazon-linux-extras install python3 && \  
yum install -y python3-devel && \  
yum clean all  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY requirements.txt /usr/src/app/  
ONBUILD RUN pip3 install --no-cache-dir -r requirements.txt  
  
ONBUILD COPY . /usr/src/app  

