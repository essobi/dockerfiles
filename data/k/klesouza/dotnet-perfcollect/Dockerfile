FROM microsoft/dotnet:2.0.3-sdk  
  
RUN apt-get update \  
&& apt-get install -y linux-tools lttng-modules-dkms liblttng-ust-dev lttng-
tools zip babeltrace  
  
RUN mkdir /code && mkdir /tmp/prof  
WORKDIR /tmp  
RUN git clone https://github.com/dotnet/corefx-tools.git --depth=1 \  
&& cd corefx-tools \  
&& git checkout src/performance/perfcollect/perfcollect \  
&& cp src/performance/perfcollect/perfcollect /tmp/perfcollect \  
&& chmod +x /tmp/perfcollect  
WORKDIR /code  
  
COPY ./scripts/* ./  
RUN chmod +x * && ls .

