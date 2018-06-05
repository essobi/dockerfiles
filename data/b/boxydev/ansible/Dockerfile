FROM ubuntu  
MAINTAINER Matthieu Mota <matthieumota@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
software-properties-common \  
figlet  
RUN apt-add-repository ppa:ansible/ansible && apt-get update && apt-get
install -y ansible  
  
RUN mkdir /app  
WORKDIR /app  
  
CMD ["ansible"]

