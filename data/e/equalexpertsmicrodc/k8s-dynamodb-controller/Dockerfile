FROM equalexpertsmicrodc/ubuntu-testing-container  
RUN mkdir /app  
WORKDIR /app  
COPY ./ /app/  
RUN ./test.sh  
  
FROM alpine  
ENV AWSCLI_VERSION=1.11.180  
RUN mkdir /app  
RUN apk add --no-cache python3 git && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
rm -r /root/.cache  
RUN pip install --upgrade --no-cache-dir pip \  
awscli=="${AWSCLI_VERSION}" \  
git+https://github.com/side8/k8s-operator  
ADD https://storage.googleapis.com/kubernetes-
release/release/v1.7.9/bin/linux/amd64/kubectl /usr/local/bin/kubectl  
RUN chmod +x /usr/local/bin/kubectl  
COPY apply delete common.sh crd.yaml /app/  
WORKDIR /app  
ENTRYPOINT ["./startup.sh"]  

