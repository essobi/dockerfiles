FROM jetbrains/teamcity-agent:latest  
  
# Update everything  
RUN apt-get update  
  
# Install command line tools required on the agent to build claimer projects  
RUN apt-get -y install mc python3.4 zip awscli  
  
# Add SSH public key  
COPY ./.ssh /root/.ssh  
  
# Pip setup  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py --user  
RUN echo "export PATH=\"~/.local/bin:\$PATH\"" >> ~/.bashrc  
  
# Set current path for active shell  
RUN export PATH="~/.local/bin:$PATH"  
  
# Install eb cli tool  
RUN ~/.local/bin/pip install awsebcli --upgrade --user && ln -s
/root/.local/bin/eb /usr/local/bin/eb  
  
# Upgrade awscli  
RUN ~/.local/bin/pip install awscli --upgrade --user  
  
# Copy setup script - run before teamcity agent starts  
COPY ./init.sh /services/

