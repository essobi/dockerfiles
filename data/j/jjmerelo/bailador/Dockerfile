FROM jjmerelo/alpine-perl6:latest  
LABEL version="3.0" maintainer="JJ Merelo <jjmerelo@GMail.com>"
perl6version="2017.11"  
  
# Set up dirs  
RUN mkdir /app  
WORKDIR /app  
RUN zef install Bailador && rakudobrew rehash  
  
# Will run this  
EXPOSE 80  
ENTRYPOINT zef install --deps-only . && bailador --config=host:0.0.0.0,port=80
easy app.pl6  
  
# Repeating mother's env  
ENV PATH="/root/.rakudobrew/bin:${PATH}"  

