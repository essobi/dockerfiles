FROM amazonlinux:2016.09  
ENV LANG en_GB.UTF-8  
WORKDIR /tmp  
  
# Install system packages  
ENV RUNTIME_PACKAGES="wget bzip2 git httpd httpd-devel"  
ENV PYTHON_BUILD_PACKAGES="gcc zlib-devel bzip2-devel sqlite sqlite-devel
openssl-devel postgresql94-devel libffi-dev readline-devel"  
RUN yum update -y && yum install -y $RUNTIME_PACKAGES $PYTHON_BUILD_PACKAGES  
  
# Get and Install yarn and Node.js  
RUN wget https://dl.yarnpkg.com/rpm/yarn.repo -O /etc/yum.repos.d/yarn.repo &&
\  
curl --location https://rpm.nodesource.com/setup_6.x | bash - && \  
yum install -y nodejs yarn && \  
yarn global add gulp-cli  
  
# Install Python from source  
ENV LD_LIBRARY_PATH="/usr/local/lib"  
RUN wget https://www.python.org/ftp/python/3.4.2/Python-3.4.2.tar.xz  
RUN tar xvf Python-3.4.2.tar.xz  
WORKDIR Python-3.4.2  
RUN ./configure --enable-shared && \  
make && \  
make install && \  
ln -s /usr/local/bin/python3 /usr/local/bin/python && \  
ln -s /usr/local/bin/pip3 /usr/local/bin/pip  
  
# Upgrade pip and then install system packages  
RUN pip install -U pip setuptools wheel  
RUN pip install mod_wsgi  
  
# Install application packages  
WORKDIR /tmp/application  
ONBUILD COPY requirements.txt /tmp/application/requirements.txt  
ONBUILD RUN pip install --no-cache-dir -r requirements.txt  
  
# Copy remainder of application  
ONBUILD COPY . /tmp/application  
  
# Setup a HEALTHCHECK  
HEALTHCHECK CMD curl -f http://localhost:80/healthcheck || exit 1  
  
# Start Apache with mod_wsgi on port 80  
EXPOSE 80  
CMD ["start-server", \  
"--port=80", \  
"--user=apache", \  
"--group=apache", \  
"--log-to-terminal", \  
"--log-level=info", \  
"--access-log", \  
"--startup-log", \  
"/tmp/application/application.py"]  
ENTRYPOINT ["mod_wsgi-express"]  

