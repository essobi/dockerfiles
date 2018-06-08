FROM athieriot/metricbeat:5.2.1  
HEALTHCHECK \--interval=5s --timeout=3s \  
CMD ps aux | grep '[m]etricbeat' || exit 1

