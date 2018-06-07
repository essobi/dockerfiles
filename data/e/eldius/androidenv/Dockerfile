FROM java:8  
  
ENV DEST_FOLDER /opt/android  
ENV ANDROID_HOME /opt/android/tools  
  
ADD ./scripts /tmp/build  
  
RUN chmod 777 -R /tmp/build && /tmp/build/install_adk.sh &&
/tmp/build/install_adk_platforms.py  
#RUN apt-get install -y unzip git && \  
# mkdir $DEST_FOLDER && \  
# cd $DEST_FOLDER && \  
# wget https://dl.google.com/android/repository/tools_r25.2.3-linux.zip && \  
# unzip tools_*.zip && \  
# rm tools_*.zip && \  
# chmod 777 -R $DEST_FOLDER/tools && \  
# mkdir -p $ANDROID_HOME/licenses && \  
# chmod 777 -R $DEST_FOLDER/tools && \  
# echo -e "\n8933bad161af4178b1185d1a37fbf41ea5269c55" >
"$ANDROID_HOME/licenses/android-sdk-license" && \  
# echo -e "\n84831b9409646a918e30573bab4c9c91346d8abd" >
"$ANDROID_HOME/licenses/android-sdk-preview-license" && \  
# echo -e "\nd975f751698a77b662f1254ddbeed3901e976f5a" >
"${ANDROID_HOME}/licenses/intel-android-extra-license" && \  
# chmod 777 -R $DEST_FOLDER/tools && \  
# echo "Android SDK installed." && \  
# python install_adk_platforms.py && \  
# echo "Android SDK configured."  
#./scripts/install_adk.sh && install_adk_platforms.py && echo "Finished!"  
  
#ONBUILD RUN python ./install_adk_platforms.py  
  
  
WORKDIR /app/build  
COPY librivox-player /app/build  
  
CMD pwd && ./gradlew clean build  

