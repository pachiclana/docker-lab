FROM python:3.12-slim
ENV TZ="Europe/Madrid"

WORKDIR /usr

#Copy the python code
COPY /multi-platform-tests/src /usr/src/

# Install python/pip
# ENV PYTHONUNBUFFERED=1
# RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
# RUN python3 -m ensurepip
# RUN pip3 install --no-cache --upgrade pip setuptools
# RUN python3 --version

# COPY src /usr/src/app/src

# RUN pip install beautifulsoup4==4.11.0
# RUN pip install requests==2.28.0
# RUN pip install pyTelegramBotAPI==4.13.0

ENTRYPOINT [ "python3", "./src/main.py"]