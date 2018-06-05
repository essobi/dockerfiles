FROM debian  
  
# Install system packages  
ENV TERM linux  
RUN apt-get update && \  
apt-get install -y \  
curl \  
git && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Install boilr  
RUN curl -sSL https://raw.githubusercontent.com/tmrts/boilr/master/install |
bash  
ENV PATH /root/bin:${PATH}  
  
ENTRYPOINT ["boilr"]  

