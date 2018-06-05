#===========================================================  
# We'll use this to build the .NET Core code.  
#===========================================================  
FROM microsoft/dotnet:2.1-sdk AS core-build-step  
  
#copy the code to the image  
COPY ./src/ /build/  
  
#move to the build directory  
WORKDIR /build/  
  
#restore and publish the bloody agent  
RUN dotnet publish \  
\--runtime linux-arm \  
\--framework netcoreapp2.0 \  
\--source https://api.nuget.org/v3/index.json \  
/build/Agent/Boondocks.Agent/Boondocks.Agent.csproj  
  
#===========================================================  
# Now start making the image that will run on the pi  
#===========================================================  
FROM boondocks/resin-dotnet:resin-raspberrypi3-dotnet210  
  
RUN [ "cross-build-start" ]  
  
#copy the built files over to the device.  
COPY \--from=core-build-step
/build/Agent/Boondocks.Agent/bin/Debug/netcoreapp2.0/linux-arm/publish/
/opt/boondocks/  
  
#copy the entry file  
COPY ./src/Agent/Boondocks.Agent/scripts/entry.sh /usr/bin/entry.sh  
  
#mark this as executable  
RUN chmod +x /usr/bin/entry.sh  
  
ENTRYPOINT [ "/usr/bin/entry.sh" ]  
  
RUN [ "cross-build-end" ]  

