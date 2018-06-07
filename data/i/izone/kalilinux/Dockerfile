FROM kalilinux/kali-linux-docker  
MAINTAINER luvres@hotmail.com.br  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN \  
echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >
/etc/apt/sources.list \  
&& echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free"
>> /etc/apt/sources.list \  
\  
&& apt-get update -y \  
&& apt-get dist-upgrade -y \  
&& apt-get clean  
  
CMD ["/bin/bash"]  

