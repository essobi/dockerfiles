FROM ubuntu:16.04  
copy ["rc", "/root/.meow/rc.temp"]  
ENV MEOW_INSTALLDIR /root  
RUN apt-get update && apt-get install -y gettext curl  
RUN curl -L git.io/meowproxy | bash  
EXPOSE 7777  
CMD ["/bin/bash","-c", "envsubst < /root/.meow/rc.temp > /root/.meow/rc &&
/root/MEOW"]  

