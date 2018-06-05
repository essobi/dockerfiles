FROM dgauch/axonivy-engine:latest  
MAINTAINER Daniel Gauch <daniel@gauch.biz>  
  
RUN sudo mkdir -p
opt/AxonIvyEngine5.1/applications/System/deployment_tool_ivy/1  
COPY deployment_tool_ivy-1.1.1.iar /opt/deployment_tool_ivy.iar  
RUN sudo unzip /opt/deployment_tool_ivy.iar -d
opt/AxonIvyEngine5.1/applications/System/deployment_tool_ivy/1  
RUN sudo rm /opt/deployment_tool_ivy.iar  

