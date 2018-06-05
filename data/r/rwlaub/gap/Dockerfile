# This Dockerfile takes the gap system image, inserts a script which  
# calls the desired gap algorithm and is configured to run that script  
FROM gapsystem/gap-docker  
COPY script.sh /home/gap  
CMD ["/home/gap/script.sh"]  

