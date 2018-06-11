FROM debian  
  
# Install curl and unzip  
RUN ["apt-get", "--quiet", "update"]  
RUN ["apt-get", "-y", "install", "curl"]  
RUN ["apt-get", "-y", "install", "unzip"]  
  
VOLUME ["/cache5.0"]  
EXPOSE 8126 8125  
ENTRYPOINT ["/opt/unitycacheserver/CacheServer/RunLinux.sh"]  
CMD ["--nolegacy", "--path", "/cache5.0"]  
  
ENV VERSION=5.4.1f1  
  
# Install cache server  
RUN ["mkdir", "-p", "/opt/unitycacheserver"]  
WORKDIR "/opt/unitycacheserver"  
RUN curl -#LO
"http://netstorage.unity3d.com/unity/649f48bbbf0f/CacheServer-${VERSION}.zip"  
RUN unzip CacheServer-${VERSION}.zip

