FROM circleci/android:api-27-alpha  
  
RUN sudo apt-get update -qq && \  
sudo apt-get install -y ant && \  
git clone https://github.com/facebook/buck.git $HOME/buck && \  
cd $HOME/buck && \  
ant  
  
ADD ./circle-ci-android-setup.sh $HOME/circle-ci-android-setup.sh  
RUN bash -c "source $HOME/circle-ci-android-setup.sh && installAndroidSDK"  
  
ADD ./warm-cache.sh $HOME/warm-cache.sh  
RUN bash "$HOME/warm-cache.sh"  

