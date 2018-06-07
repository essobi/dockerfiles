FROM elementar/aws-cli  
MAINTAINER Elementar Sistemas <contato@elementarsistemas.com.br>  
  
CMD aws elb register-instances-with-load-balancer \  
\--load-balancer-name "$LOAD_BALANCER_NAME" \  
\--instances "$(curl -s --fail http://169.254.169.254/latest/meta-
data/instance-id)"

