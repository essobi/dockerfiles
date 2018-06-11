FROM redis:latest  
  
MAINTAINER info@whereuat.ninja  
  
ENV WHEREUAT_API_APP_ENV development  
  
COPY ./docker/config/redis.${WHEREUAT_API_APP_ENV}.conf /etc/redis.conf  
  
EXPOSE 6379  
ENTRYPOINT ["redis-server", "/etc/redis.conf"]  
  
# To Build:  
# docker build -f .\docker\redis.dockerfile -env
<development|production|staging> whereuatninja/redis .  
# To Run:  
# docker run -d -p 6379:6379 --name redis whereuatninja/redis

