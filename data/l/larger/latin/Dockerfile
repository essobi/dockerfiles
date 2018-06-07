From ubuntu:14.04  
RUN apt-get update  
ADD
https://raw.githubusercontent.com/pixelorz/binary/master/lantern%20for%20ubuntu%2014.04/linux%20server/lantern_linux_amd64
/lantern  
RUN chmod +x /lantern  
EXPOSE 8787  
ENTRYPOINT [ "/lantern", "-addr", "0.0.0.0:8787" ]

