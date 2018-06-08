# My setup  
FROM fedora  
COPY [".", "/app"]  
RUN ["/app/setup/force.sh", "docker"]  
ENTRYPOINT ["/app/setup/docker/entrypoint.py", "--setup"]  
CMD ["--", "bash"]  

