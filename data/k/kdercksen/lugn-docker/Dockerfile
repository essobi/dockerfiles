FROM debian:latest  
MAINTAINER Koen Dercksen <mail@koendercksen.com>  
# Install cowsay  
RUN apt-get update && apt-get install -y cowsay --no-install-recommends  
# cowsay installs to /usr/games  
ENV PATH /usr/games:$PATH  
COPY ./run.sh /run.sh  
ENTRYPOINT ["/run.sh"]  
# Default text  
CMD ["EXAMPLE"]  

