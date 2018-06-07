# Use this image as a base  
FROM niaquinto/gradle  
  
MAINTAINER "dewmal@egreen.io"  
# In case someone loses the Dockerfile  
RUN rm -rf /etc/Dockerfile  
ADD Dockerfile /etc/Dockerfile  
  
# Add your desired user and group  
#RUN groupadd mytrip  
#RUN useradd -s /bin/bash -m -d /usr/bin/app -g mytrip mytrip  
# Set your desired user as default  
#USER mytrip  
COPY . /usr/bin/app  
  
#RUN /usr/lib/gradle clean installC  
RUN mkdir /root/chitscanner  
  
EXPOSE 8461  
# Set your default behavior  
ENTRYPOINT ["gradle"]  
CMD ["-PmainClass=io.egreen.backoffice.service.Main", "service:execute"]  
#docker run -itd -p8461:8461 --name='ct_back_office' --restart=always --add-
host mongodb:`/sbin/ip route|awk '/default/ { print $3}'`
dewmal/ct_back_office  

