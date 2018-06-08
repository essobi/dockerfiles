# My setup  
FROM ubuntu:rolling  
COPY [".", "/app"]  
RUN ["/app/setup/force.sh", "docker"]  
ENTRYPOINT ["/app/setup/docker/entrypoint.py", "--setup"]  
CMD ["--", "bash"]  

