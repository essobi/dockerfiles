FROM openstf/stf:v2.0.1  
  
ENV STF_PUBLIC_IP 127.0.0.1  
  
EXPOSE 7100  
  
USER root  
  
RUN dpkg --add-architecture i386 \  
&& apt-get -yq update \  
&& apt-get -yq install libncurses5:i386 libstdc++6:i386 zlib1g:i386 --no-
install-recommends android-tools-adb \  
&& apt-get clean  
  
CMD ["stf", "local", "--public-ip ${STF_PUBLIC_IP}"]  

