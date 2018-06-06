FROM scratch  
  
ADD bin/dagger /  
  
ENTRYPOINT ["/dagger", "--working-dir=/data"]  
  
# docker build -t dogik/dagger -f Dockerfile .  
# docker run -it -v /data/project:/data:ro -v
/var/run/docker.sock:/var/run/docker.sock dogik/dagger

