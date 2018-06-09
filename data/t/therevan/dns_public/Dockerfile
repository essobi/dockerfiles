FROM debian:stretch  
RUN apt-get update && apt-get upgrade -y  
  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
LABEL name="dns"  
LABEL description="Bind 9 DNS-Server"  
LABEL version="2.1.180211"  
LABEL author="Tim Schlottmann <tschlottmann@gmail.com>"  
RUN apt-get install bind9 -y  
  
EXPOSE 53  
EXPOSE 53/UDP  
  
CMD ["named","-g"]  
  
COPY config /etc/bind

