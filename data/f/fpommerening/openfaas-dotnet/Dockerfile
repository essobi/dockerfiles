FROM microsoft/dotnet:2.0-sdk-jessie AS builder  
  
WORKDIR /app  
COPY src /app  
RUN dotnet restore Alexa.csproj  
RUN dotnet publish --configuration Release --output ./out  
  
FROM microsoft/dotnet:2.0-runtime-jessie  
LABEL maintainer "frank@pommerening-online.de"  
  
EXPOSE 8080  
WORKDIR /app/  
RUN echo "Pulling watchdog binary from Github." \  
&& curl -sSL
https://github.com/openfaas/faas/releases/download/0.6.9/fwatchdog >
/usr/bin/fwatchdog \  
&& chmod +x /usr/bin/fwatchdog  
  
ENV REFRESHED_AT 2018-01-28  
COPY \--from=builder /app/out/* ./  
  
ENV fprocess="dotnet ./Alexa.dll"  
CMD ["fwatchdog"]

