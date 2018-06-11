FROM python:3.6.5-alpine3.7  
RUN apk update && \  
apk add curl bind-tools bash && \  
rm -rf /var/cache/apk && \  
pip install speedtest-cli httpie && \  
rm -rf ~/.cache  
  
CMD ["/usr/bin/env", "bash"]  

