FROM alpine  
  
# Install nginx  
RUN apk add --no-cache nginx curl && \  
mkdir -p /run/nginx/  
  
# Add configuration files  
ADD conf.d/ /etc/nginx/conf.d/  
ADD snippets.d/ /etc/nginx/snippets.d/  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD LICENSE /etc/nginx/LICENSE  
  
# Run on port 80  
EXPOSE 80  
HEALTHCHECK \--start-period=30s CMD curl -f http://localhost/ || exit 1  
CMD ["nginx", "-c", "/etc/nginx/nginx.conf"]

