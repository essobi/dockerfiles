FROM quay.io/coreos/kube-state-metrics:v1.3.0  
EXPOSE 8080  
EXPOSE 8081  
ENTRYPOINT ["/kube-state-metrics", "--port=8080", "--telemetry-port=8081", "--
apiserver=http://172.20.1.30:8080"]  

