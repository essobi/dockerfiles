# sudo docker build -t k8s-probe-health .  
# sudo docker run -e NAMESPACE="kube-system" -e
KUBE_API_URL="https://stakater3-kube-api.stakater.com:6443" -i --rm -v
~/.kube:/root/.kube/ -v
~/IdeaProjects/FreemiumF8Infrastructure/input/:/root/kat_output/ --name
k8s-probe-health k8s-probe-health  
FROM stakater/go-k8s  
ADD . /go/k8s-probe-health  
RUN chmod +x /go/k8s-probe-health/bootstrap.sh  
CMD ["sh", "-c", "/go/k8s-probe-health/bootstrap.sh"]  

