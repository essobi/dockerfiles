FROM node:9.2.0  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.1/dumb-
init_1.1.1_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY package.json /app/  
RUN yarn install --production  
COPY . /app  
  
COPY id_rsa_kbasestage_cicd /root/.ssh/id_rsa  
COPY id_rsa_kbasestage_cicd.pub /root/.ssh/id_rsa.pub  
  
COPY id_rsa_success_stage_cicd /root/.ssh/id_rsa_success  
COPY id_rsa_success_stage_cicd.pub /root/.ssh/id_rsa_success.pub  
  
COPY id_rsa_mta_infra /root/.ssh/id_rsa_mta_infra  
  
RUN chmod 600 /root/.ssh/id_rsa  
RUN chmod 600 /root/.ssh/id_rsa_success  
RUN chmod 600 /root/.ssh/id_rsa_mta_infra  
  
RUN ssh-keyscan -H github.com >> ~/.ssh/known_hosts  
  
WORKDIR /app/github-kbase  
RUN eval "$(ssh-agent -s)" && \  
ssh-add /root/.ssh/id_rsa_success && \  
git clone git@github.com:docker/success.git  
  
WORKDIR /app/github-kbase  
RUN eval "$(ssh-agent -s)" && \  
ssh-add /root/.ssh/id_rsa && \  
git clone git@github.com:docker/kbase-stage.git  
  
WORKDIR /app/github-kbase  
RUN eval "$(ssh-agent -s)" && \  
ssh-add /root/.ssh/id_rsa_mta_infra && \  
git clone git@github.com:docker/mta-infrastructure.git  
  
RUN git config --global user.email "peter.mckee@docker.com"  
RUN git config --global user.name "Peter"  
  
WORKDIR /app  
  
EXPOSE 80  
# ENTRYPOINT ["/bin/bash"]  
CMD [ "dumb-init", "node", "server.js" ]  

