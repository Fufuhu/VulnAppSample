FROM python:3.8-slim-buster

RUN useradd vuln && \
    mkdir -p /home/vuln && \
    chown vuln:vuln /home/vuln
USER vuln
RUN mkdir -p /home/vuln/.local/bin
ENV PATH $PATH:/home/vuln/.local/bin
EXPOSE 8000
WORKDIR /home/vuln
COPY requirements.txt ./
COPY vulnapp ./
RUN pip install -r requirements.txt
RUN python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000