FROM circleci/python:3.6.1  
#install gcloud sdk with all stuff  
RUN export CLOUDSDK_CORE_DISABLE_PROMPTS=1 && \  
curl https://sdk.cloud.google.com | bash  
  
#automatic include of google cloud sdk  
RUN echo "source /home/circleci/google-cloud-sdk/completion.blibmcrypt-dev &&
sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*ash.inc" >> /home/circleci/.bashrc && \  
echo "source /home/circleci/google-cloud-sdk/path.bash.inc" >>
/home/circleci/.bashrc  
  
#install custom gcloud sdk components  
RUN bash -c "source /home/circleci/google-cloud-sdk/path.bash.inc && gcloud
--quiet components install kubectl beta docker-credential-gcr"  
  
RUN sudo apt-get remove -y libpng-dev

