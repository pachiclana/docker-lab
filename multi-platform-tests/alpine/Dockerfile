FROM python:3.12-slim
ENV TZ="Europe/Madrid"

WORKDIR /usr

#Copy the python code
COPY /multi-platform-tests/src /usr/src/

#Entrypoint
ENTRYPOINT [ "python3", "./src/main.py"]