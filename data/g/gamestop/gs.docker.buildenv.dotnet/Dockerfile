FROM microsoft/dotnet:2.1-sdk  
  
RUN apt-get update \  
&& apt-get install \--reinstall make \  
&& apt-get install build-essential -y \  
&& apt-get install awscli -y \  
&& apt-get install jq -y \  
&& apt-get install zip -y \  
&& apt-get install nuget -y  
  
# Install nodejs 8 and register artifactory repo  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs  
  
# Install yq  
RUN wget "https://bootstrap.pypa.io/get-pip.py" -O /tmp/get-pip.py \  
&& python /tmp/get-pip.py \  
&& pip install yq  

