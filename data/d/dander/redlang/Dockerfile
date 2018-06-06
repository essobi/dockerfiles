FROM 32bit/debian:latest  
  
LABEL Description="This image will run the red console in a debian
environment."  
  
RUN apt-get update && apt-get install -y \  
libcurl3 \  
&& wget http://static.red-lang.org/dl/auto/linux/red-latest -O /bin/red \  
&& chmod +x /bin/red \  
&& echo "q" | /bin/red  
  
CMD [ "/bin/red" ]  

