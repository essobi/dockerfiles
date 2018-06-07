FROM generik/ansible:v2.3.1.0-1  
ARG helmbinary=helm-v2.5.1-linux-amd64.tar.gz  
ADD https://storage.googleapis.com/kubernetes-helm/${helmbinary} .  
RUN ls -l && tar -zxvf ${helmbinary} && mv linux-amd64/helm /usr/bin/ && chmod
+x /usr/bin/helm  
ADD https://storage.googleapis.com/kubernetes-
release/release/v1.6.6/bin/linux/amd64/kubectl /usr/bin/  
RUN chmod +x /usr/bin/kubectl  
RUN pip install boto3  
RUN pip install awscli==1.11.127  

