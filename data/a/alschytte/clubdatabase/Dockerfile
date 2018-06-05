# sudo docker build -t alschytte/clubdatabase . # in /app/clubdatabase/scripts
directory  
# sudo docker login alschytte # provide password  
# sudo docker push alschytte/clubdatabase # push it to docker.io  
FROM debian:latest  
MAINTAINER Allan Schytt "as@int.fountain-house-dk"  
COPY "/scripts/stackscript.sh" "/stackscript.sh"  
RUN bash "/stackscript.sh"

