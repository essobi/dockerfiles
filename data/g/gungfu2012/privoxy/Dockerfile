#privoxy  
From ubuntu  
  
MAINTAINER gungfu2012@gmail.com  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install
privoxy && apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN chmod 777 /etc/privoxy  
RUN chmod 777 /etc/privoxy/*  
RUN chmod 777 /etc/privoxy/templates/*  
COPY config /etc/privoxy/  
RUN chmod 777 /etc/privoxy/config  
  
EXPOSE 8118  
ENTRYPOINT privoxy --no-daemon /etc/privoxy/config  

