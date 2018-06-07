FROM tutum/logrotate:latest  
  
HEALTHCHECK \--interval=5s --timeout=3s \  
CMD ps aux | grep '[c]rond' || exit 1

