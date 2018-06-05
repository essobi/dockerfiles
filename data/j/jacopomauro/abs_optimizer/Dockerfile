FROM python:3-stretch  
MAINTAINER Jacopo Mauro  
  
# install dependencies and useful commands  
RUN \  
# adding erlang repository entry  
wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb && \  
dpkg -i erlang-solutions_1.0_all.deb && \  
rm erlang-solutions_1.0_all.deb && \  
# install packages  
apt-get update && \  
apt-get install -y \  
erlang \  
openjdk-8-jre-headless \  
time \  
nano && \  
rm -rf /var/lib/apt/lists/* && \  
pip install \  
click \  
requests  
  
# if the compilation of abs tools is needed  
RUN \  
apt-get update && apt-get install -y \  
make \  
default-jdk \  
ant && \  
cd / && \  
git clone \--depth=1 https://github.com/abstools/abstools.git && \  
cd abstools && \  
make  
ENV PATH /abstools/frontend/bin/bash:$PATH  
  
# install the absc compiler from the dockerhub image  
#COPY --from=abslang/collaboratory:latest
/usr/local/lib/frontend/dist/absfrontend.jar /absfrontend.jar  
#RUN echo 'java -Xmx512m -jar /absfrontend.jar "$@"' > /usr/bin/absc && \  
# chmod 700 /usr/bin/absc  
# clone abs_optimizer  
RUN git clone \--depth=1 -b demonstrator2
https://github.com/HyVar/abs_optimizer.git  
  
# expose port 9001 for the server  
EXPOSE 9001  
WORKDIR /abs_optimizer  
CMD ["python","docker/server.py", "--port", "9001"]  
  

