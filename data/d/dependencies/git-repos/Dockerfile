FROM python:3.6-alpine  
  
RUN apk --no-cache add git build-base  
  
# add a non-root user and give them ownership  
RUN adduser -D -u 9000 app && \  
# repo  
mkdir /repo && \  
chown -R app:app /repo && \  
# app code  
mkdir /usr/src/app && \  
chown -R app:app /usr/src/app  
  
RUN pip install ruamel.yaml semantic_version  
  
# add the pullrequest utility to easily create pull requests on different git
hosts  
WORKDIR /usr/src/app  
ENV DEPS_VERSION=2.3.0  
ADD https://github.com/dependencies-
io/pullrequest/releases/download/${DEPS_VERSION}/deps_${DEPS_VERSION}_linux_amd64.tar.gz
.  
RUN mkdir deps && \  
tar -zxvf deps_${DEPS_VERSION}_linux_amd64.tar.gz -C deps && \  
ln -s /usr/src/app/deps/deps /usr/local/bin/deps  
  
# run everything from here on as non-root  
USER app  
  
RUN git config --global user.email "bot@dependencies.io"  
RUN git config --global user.name "Dependencies.io Bot"  
  
ADD src/ /usr/src/app/  
  
WORKDIR /repo  
  
ENTRYPOINT ["python", "/usr/src/app/entrypoint.py"]  

