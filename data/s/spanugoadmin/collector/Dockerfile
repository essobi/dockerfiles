#  
# Collector Dockerfile  
#  
# image updated to spanugoadmin/collector:latest  
FROM openjdk:8-jdk-alpine  
  
ENV ROOT_DIR /opt/package  
  
# setup directories  
RUN mkdir -p $ROOT_DIR/install  
RUN mkdir -p $ROOT_DIR/config  
RUN mkdir -p $ROOT_DIR/logs  
RUN mkdir -p $ROOT_DIR/scripts  
RUN mkdir -p $ROOT_DIR/cert  
RUN mkdir -p $ROOT_DIR/runtime/certificates  
RUN mkdir /root/.aws  
  
# Install.  
RUN apk update  
RUN apk add --no-cache --virtual=build-dependencies \  
tzdata \  
ca-certificates \  
curl \  
gcc \  
musl-dev \  
libffi-dev \  
openssl-dev \  
build-base \  
libc6-compat \  
linux-headers  
RUN apk add --no-cache \  
openssl \  
python \  
python-dev \  
py2-pip \  
redis \  
tcpdump \  
vim  
RUN apk add --no-cache \  
bash bash-doc bash-completion \  
util-linux pciutils usbutils coreutils binutils findutils grep curl \  
man man-pages mdocml-apropos less less-doc  
  
RUN pip install awscli  
RUN pip install boto  
RUN pip install boto3  
RUN pip install boto3-extensions  
RUN pip install jumpssh  
RUN pip install logger  
RUN pip install pyopenssl  
RUN pip install requests  
  
# setup supervisord  
RUN pip install supervisor  
RUN mkdir /etc/supervisor/  
RUN mkdir /etc/supervisor/conf.d/  
COPY conf/supervisord.conf /etc/supervisor/supervisord.conf  
  
RUN gcc --version  
RUN pip install avro  
RUN pip install twisted  
RUN pip install txredis  
RUN pip install txredisapi  
RUN pip install scandir==1.2  
RUN pip install ipython==5.5.0  
RUN pip install pyflakes  
  
COPY scripts/aws_configure.sh $ROOT_DIR/scripts/aws_configure.sh  
COPY scripts/process_mgr.py $ROOT_DIR/scripts/process_mgr.py  
COPY scripts/control_server.py $ROOT_DIR/scripts/control_server.py  
COPY scripts/aws_configure.sh $ROOT_DIR/scripts/aws_configure.sh  
COPY cert/SpanugoJKS.jks $ROOT_DIR/cert/  
COPY conf/rc.local /etc/rc.local  
  
RUN pyflakes $ROOT_DIR/scripts  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR $ROOT_DIR  
  
# Start supervisor  
CMD ["sh", "-c", "/usr/bin/supervisord; bash"]  

