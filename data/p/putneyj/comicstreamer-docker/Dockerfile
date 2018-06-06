FROM debian  
  
MAINTAINER putneyj  
  
ENV PORT 32500  
ENV WEBROOT ""  
RUN apt-get update && apt-get install python python-pip python-dev git
libjpeg-dev zlib1g-dev -y  
  
# Run commands as the comicstreamer user  
RUN adduser \  
\--disabled-login \  
\--shell /bin/bash \  
\--gecos "" \  
comicstreamer  
  
# Copy & rights to folders  
COPY run.sh /home/comicstreamer/run.sh  
  
RUN chmod 777 /home/comicstreamer/run.sh  
  
# create the comics directory  
RUN mkdir /comics && chown comicstreamer /comics  
  
WORKDIR /home/comicstreamer  
  
RUN git clone https://github.com/davide-romanini/ComicStreamer.git  
  
WORKDIR /home/comicstreamer/ComicStreamer  
  
RUN pip install `cat requirements.txt`  
  
RUN chown comicstreamer -R .  
  
USER comicstreamer  
  
RUN paver libunrar  
  
# Expose default port : 32500  
EXPOSE ${PORT}  
  
VOLUME "/comics"  
  
ENTRYPOINT ["/home/comicstreamer/run.sh"]  

