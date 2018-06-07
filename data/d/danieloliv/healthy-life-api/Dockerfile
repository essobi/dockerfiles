# Build  
# docker build -t danieloliv/healthylife-api .  
# Run  
# docker run -it --rm --name healthylife_api -p 3000:3000
danieloliv/healthylife-api  
FROM rails:onbuild  
RUN chmod +x ./entrypoint.sh  
  
ENTRYPOINT ["./entrypoint.sh"]  

