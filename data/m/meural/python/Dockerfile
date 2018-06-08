FROM python:2-slim-stretch  
  
# We install essentails  
RUN apt-get update -y  
RUN apt-get install -y build-essential \  
curl \  
software-properties-common \  
git \  
sudo \  
unzip  
  
# Now we install dependences  
RUN apt-get install -y libpq-dev \  
imagemagick \  
libmagickwand-dev \  
python-imaging \  
libgeoip-dev \  
ffmpegthumbnailer \  
ffmpeg \  
gifsicle  
  
# Install AWS CLI  
RUN curl -o /tmp/awscli-bundle.zip https://s3.amazonaws.com/aws-cli/awscli-
bundle.zip  
RUN unzip /tmp/awscli-bundle.zip -d /tmp/  
RUN sudo /tmp/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
RUN rm /tmp/awscli-bundle.zip && rm -rf /tmp/awscli-bundle  
  
# Install ECS CLI  
RUN sudo curl -o /usr/local/bin/ecs-cli https://s3.amazonaws.com/amazon-ecs-
cli/ecs-cli-linux-amd64-latest  
RUN sudo chmod +x /usr/local/bin/ecs-cli  
  
RUN mkdir -p /var/www/  
  
WORKDIR /var/www/  
  

